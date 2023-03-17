import requests
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from loader.models import GoogleSheetTable
from data_recipient import get_new_data
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv(override=True)

# Включить работу по расписанию
scheduler_plan = BackgroundScheduler()  ## Создание экземпляра планировщика


# Отправка сообщения в виде  request на api telegramm
def sendMessage(orders_with_past_delivery_times):
    # Токен вашего бота, настраивается в .env
    token = os.environ.get('TOKEN')
    # Номер чата (ваш id пользователя) настраивается в .env
    chatid = os.environ.get('CHATID')
    base_url = 'https://api.telegram.org/bot'
    #собираем url
    url = f"{base_url}{token}/sendMessage?parse_mode=HTML"
    # Собираем сообщение
    message = f"У данных заказов истек срок дотсавки:\n"
    for i in orders_with_past_delivery_times:
        message += f"№:{i}\n"
    # отправляем
    requests.post(url, data={
        "chat_id": chatid,
        "text": message
    })


try:
    # Планировщик использует DjangoJobStore ()
    scheduler_plan.add_jobstore(DjangoJobStore(), "default")


    # Установить задачи по времени, метод выбора - интервал, временной интервал - 15 минут
    # В данном случае настройка идет в минутах и значение вытаскивается из переменных окружения
    # @register_job(scheduler_plan, 'cron', day_of_week='mon-fri', hour='8', minute='30', second='10',id='task_time')
    @register_job(scheduler_plan, "interval", minutes=int(os.environ.get('UPDATEINTERVAL')), replace_existing=True)
    def my_job():
        #Данная задача исполняется один раз в заданный промежуток времени
        concurrent_date = datetime.now().date()
        orders_with_past_delivery_times = []
        # так как данных не много, я не стал делать валидацию и поиск новых и изменённых данных
        # Мы просто удаляем старые данные
        GoogleSheetTable.objects.all().delete()
        # Получаем новые
        data = get_new_data()
        objects = []
        # Создаем пулл для bulk create
        for item in data:
            new_row = GoogleSheetTable(
                order_number=item["order_number"],
                order_cost_in_dollars=item["order_cost_in_dollars"],
                delivery_time=item["delivery_time"],
                order_cost_in_rubles=item['order_cost_in_rubles'])
            objects.append(new_row)
            # попутно ищем заказы у которых истёк срок доставки
            if concurrent_date > item["delivery_time"]:
                orders_with_past_delivery_times.append(item["order_number"])
        # Записываем новые данные в нашу модель
        GoogleSheetTable.objects.bulk_create(objects)
        # Отсылаем сообщение в бота, с номерами заказов у которых истёк срок доставки
        sendMessage(orders_with_past_delivery_times)
        # это для лога, просто чтобы видеть что всё работает.
        print('success')


    register_events(scheduler_plan)
    scheduler_plan.start()
except Exception as e:
    print(e)
    # Остановить таймер в случае ошибки
    scheduler_plan.shutdown()

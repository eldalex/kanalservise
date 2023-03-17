from django.db import models

#Модель для хранения данных таблицы
class GoogleSheetTable(models.Model):
    order_number = models.IntegerField(verbose_name='номер заказа')
    order_cost_in_dollars = models.IntegerField(verbose_name='стоимость заказа в долларах')
    delivery_time = models.DateField(verbose_name='срок поставки')
    order_cost_in_rubles = models.FloatField(verbose_name='стоимость заказа в долларах')


    def __str__(self):
        return "Таблица заказов"
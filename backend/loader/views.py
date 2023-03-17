from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *
from django.http import HttpResponse

##################################################################
########################## ВНИМАНИЕ ##############################
##################################################################
'''
Нижняя строка должна быть закоментированна при первом запуске docker-compose up!
Она используется для инициализации рассписания, но выдаёт ошибку при первой миграции 
потому что обращается к таблице которая еще не существует.
'''
##################################################################
from crontab import scheduler_plan
##################################################################
def test(request):
    return HttpResponse('Hello')

#Endpoint получения данных из django restframework
@api_view(['GET'])
def get_current_table(request):
    # Получить все записи
    data = GoogleSheetTable.objects.all()
    # Сериализуем
    serializer = TableSerializer(data, context={'request':request}, many=True)
    # Отдаём.
    return Response(serializer.data)
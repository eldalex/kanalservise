from django.contrib import admin
from django.urls import path, re_path
from loader.views import test, get_current_table
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/table/$', get_current_table),
    path('', test),
]

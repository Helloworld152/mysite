"""定义learning_logs的URL模式"""

from django.conf.urls import url
from django.urls import path

from .views import index
app_name = 'common'
urlpatterns = [
    #主页
    path('', index, name='index'),
]
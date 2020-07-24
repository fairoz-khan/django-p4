from django.urls import path
from . import views
app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/<name>', views.home, name='home'),
    path('facto/<num>', views.facto, name='facto'),
]
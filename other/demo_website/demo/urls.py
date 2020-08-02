from django.conf.urls import url
from . import views

app_name = 'demo'

urlpatterns = [
   
    url(r'^$',views.index, name='index'),
    # url(r'^get_rows/',views.get_rows, name='get_rows'),
]








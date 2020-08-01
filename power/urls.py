from django.conf.urls import url
from . import views

app_name = 'power'

urlpatterns = [
   
    url(r'^$',views.index, name='index'),
    url(r'^user_dash/',views.user_dash, name='user_dash'),
 
    # url(r'^get_data/(?P<id>\d+)/',views.scraping, name='scraping'), 

    # url(r'^enable_notifications/',views.enable_notifications, name='enable_notifications'), 
    # url(r'^scraping/',views.scraping, name='scraping'), 
    # url(r'^scrap_data/',views.scrap_data, name='scrap_data'),   
]








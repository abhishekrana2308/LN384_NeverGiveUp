from django.conf.urls import url
from . import views

app_name = 'power'

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^govt_login/',views.govt_login, name='govt_login'),
    url(r'^govt_signup/',views.govt_signup, name='govt_signup'),
    url(r'^user_login/',views.user_login, name='user_login'),
    url(r'^user_signup/',views.user_signup, name='user_signup'),
    url(r'^logout/',views.logout, name='logout'),   
    url(r'^add_board/',views.add_board, name='add_board'),   
    # url(r'^view_board/',views.view_board, name='view_board'),   
    url(r'^govt_dash/',views.govt_dash, name='govt_dash'),
    url(r'^user_dash/',views.user_dash, name='user_dash'),
    url(r'^edit_profile/',views.edit_profile, name='edit_profile'),   
    url(r'^search/',views.search, name='search'),   
    url(r'^get_data/(?P<id>\d+)/',views.scraping, name='scraping'), 
    url(r'^change_password/',views.change_password, name='change_password'), 
    url(r'^enable_notifications/',views.enable_notifications, name='enable_notifications'), 
    url(r'^scraping/',views.scraping, name='scraping'), 
    url(r'^scrap_data/',views.scrap_data, name='scrap_data'), 



    url(r'^analysis/',views.analysis, name='analysis'),
    url(r'^save_table/',views.save_table, name='save_table'),
    url(r'^get_data/',views.get_data, name='get_data'),
    url(r'^history/',views.history, name='history'),
    url(r'^alert/',views.alert, name='alert'),
    url(r'^getalert/',views.getalert, name='getalert'),
    url(r'^sendmailall/',views.sendmailall, name='sendmailall'),
    url(r'^addalert/',views.addalert, name='addalert'),


]





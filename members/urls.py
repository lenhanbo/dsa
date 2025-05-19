from django.urls import path
from . import views


app_name = 'testing'


urlpatterns = [
    
    path('homepage/', views.get_homepage, name='abc'),
    path('info/<int:id>', views.get_info, name = 'get_info'),
    path('submitform', views.submit_form),
    path('delete_comment/<int:id>', views.delete_comment),
    path('timban/', views.timban, name = 'timban'),
    
]
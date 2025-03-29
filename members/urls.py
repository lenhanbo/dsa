from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.members, name='abc'),
    path('homepage/info/<int:id>', views.get_info, name = 'get_info')
]
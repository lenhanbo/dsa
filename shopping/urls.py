from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_listview.as_view(), name = 'item_list'),
    path('item/<int:pk>', views.item_detailview.as_view(),{'ok': '1'},  name = 'item_detail'),
    path('user/<int:pk>', views.user_detailview.as_view(), name = 'user_detail'),
    path('myitem/', views.user_item.as_view(), name = 'user_item')
]
from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homepage.as_view(), name = 'homepage'),
    path('document/<int:pk>/', views.document_detail.as_view(), name = 'document_detail'),
    path('create_blog/', views.create_blog_form, name='create_blog'),
    path('create_blog/submitform/', views.submit_blog_form, name ='submit_blog_form'),
    path('document/<int:pk>/download/', views.download_file, name="download_file"),
    path('document/<int:pk>/submitcomment', views.submit_comment_form, name="submit_comment_form"),
    path('document/<int:pk>/deletecomment/<int:id>', views.delete_comment, name='delete_comment'),
    path('document/<int:pk>/deleteblog', views.delete_blog, name="delete_blog"),
]
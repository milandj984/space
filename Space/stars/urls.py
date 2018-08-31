from django.urls import path
from . import views

app_name = 'stars'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('user_login/', views.user_login, name='user_login'),
    path('new_group/', views.new_group, name='new_group'),
    path('group_details/<str:slug>', views.group_details, name='group_details'),
    path('post/', views.post, name='post'),
    path('my_groups/', views.my_groups, name='my_groups'),
    path('upload/', views.upload, name='upload'),
    path('space_uploads', views.space_uploads, name='space_uploads'),
]
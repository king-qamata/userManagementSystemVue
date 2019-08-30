from django.urls import path, re_path
from userManagement import views

urlpatterns = [
    path('getList', views.get_list),
    path('removeUser', views.remove_user),
    path('editUser', views.edit_user),
    path('addUser', views.add_user),
    path('getADList', views.get_advertisement_list),
    re_path(r'^upload/', views.upload),
    re_path(r'photos/*', views.get_photo)
]

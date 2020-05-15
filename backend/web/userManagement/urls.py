from django.urls import path, re_path
from userManagement import views
from .views import HomePageView
from .views import UserCreate, LoginView, UserDetail, ProfileView, ProfileDetail

urlpatterns = [
    path('', views.UserListView.as_view()),
    path('<int:pk>', UserDetail.as_view()),
    path('profiles', ProfileView.as_view()),
    path('profiles/<int:pk>', ProfileDetail.as_view()),
    path('home', HomePageView.as_view(), name='home'),
    path('getList', views.get_list),
    path('removeUser', views.remove_user),
    path('editUser', views.edit_user),
    path('addUser', views.add_user),
    path('getADList', views.get_advertisement_list),
    re_path(r'^upload/', views.upload),
    re_path(r'photos/*', views.get_photo),
    path("signup/", UserCreate.as_view(), name="user_create"),
    path("signin/", LoginView.as_view(), name="login"),
    path('Login', views.login),
    path('userCreate', views.user_create)
]

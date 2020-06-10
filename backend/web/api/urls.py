from django.urls import include, path
from .views import AdministratorView, ModeratorView, ModeratorDetail


urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('users/', include('userManagement.urls')),
     # Administrators
    path('administrators', AdministratorView.as_view()),

    # Moderators
    path('moderators', ModeratorView.as_view()),
    path('moderators/<int:pk>', ModeratorDetail.as_view()),
]

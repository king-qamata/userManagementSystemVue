from django.db import models
from general.created_modified import CreatedModified
from django.conf import settings
# Create your models here.



class Administrator(CreatedModified):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='administrator_profile')

    def __str__(self):
        return self.user.email


class Moderator(CreatedModified):
    sponsor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='sponsored_moderators')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='moderator_profile')

    def __str__(self):
        return self.user.email

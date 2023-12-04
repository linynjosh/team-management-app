from django.db import models
from .constants import MAX_FIRST_NAME_LENGTH, MAX_LAST_NAME_LENGTH, PHONE_LENGTH, MAX_EMAIL_LENGTH

# Create your models here.

class Member(models.Model):
    first_name = models.CharField(max_length=MAX_FIRST_NAME_LENGTH)
    last_name = models.CharField(max_length=MAX_LAST_NAME_LENGTH)
    phone = models.CharField(max_length=PHONE_LENGTH)
    email = models.CharField(max_length=MAX_EMAIL_LENGTH)
    is_admin = models.BooleanField()

    class Meta:
        unique_together = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

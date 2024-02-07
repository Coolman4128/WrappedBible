from django.db import models

# Create your models here.
class Users(models.Model):
    UserId = models.CharField(max_length = 255)
    User_Name = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)

    def __str__(self):
        return self.UserId

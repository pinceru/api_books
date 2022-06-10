from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    telephone = models.CharField(max_length=8)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name

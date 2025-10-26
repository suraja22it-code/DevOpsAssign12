from django.db import models

class Login(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'login'

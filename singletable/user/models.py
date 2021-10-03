from django.db import models

# Create your models here.
class User(models.Model):
    userId = models.CharField(max_length="100")
    userPw = models.CharField(max_length="100")
    reUserPw = models.CharField(max_length="100")
    realName = models.CharField(max_length="100")
    nickName = models.CharField(max_length="100")
    Email = models.CharField(max_length="100")
    birthDay = models.CharField(max_length="100")
    schoolCode = models.CharField(max_length="100")
    authCode = models.CharField(max_length="100")
    def __str__(self): 
        return self.userId
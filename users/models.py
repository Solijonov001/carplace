from django.db import models
from django.contrib.auth.models import AbstractUser




# Create your models here.
class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars',null=True,blank=True)
    profession = models.CharField(max_length=100,null=True,blank=True)
    bio = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.username





"""
1.Default Users Modelini extend qilish
class CustomUser(User)
    avatar = ...
    
2. AbstractUser Modelini extend qilish
3. AbstractBaseUser Modelin9i extend qilish
4. Alohida Profile modelini ochib, default One2One qilish
"""

from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager

# Create your models here.

from custom_accounts.storage import OverwriteStorage
custom_store = OverwriteStorage()

class MyAccountManager(BaseUserManager):
    
    def create_user(self,email,username,password=None):

        user=self.model(
            email=self.normalize_email(email),
            username=username,
        )   
        user.set_password(password)
        user.save(using=self._db)

        return user
        
    def create_superuser(self,email,username,password): 
        
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )   
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=100,unique=True)
    username = models.CharField(max_length=50)
    avatar = models.ImageField(storage=custom_store, null=True, default='avatar.svg')
    phone = models.CharField(max_length=200, null=True, blank=True)
    
    # Required
    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = MyAccountManager()
    
    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Custom user'
        verbose_name_plural = 'Custom Users'

    def has_perm(self, perm, obj=None):
        return self.is_superadmin
    
    def has_module_perms(self, app_label):
        return True
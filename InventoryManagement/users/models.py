from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username,email, password):
        if not username:
            raise ValueError("Enter a valid Email address") 
        if not email:
            raise ValueError("Enter a valid Email address") 
        user = self.model(username= username ,email= self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, password):
        user = self.create_user(email,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user

# class Role(models.Model):
#     ROLE_CHOICES = [
#         ('Admin', 'Admin'),
#         ('Manager', 'Manager'),
#         ('Staff', 'Staff'),
#     ]
#     name = models.CharField(max_length=50, choices=ROLE_CHOICES, unique=True)
#     description = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name
    
class User(AbstractUser):
    email = models.EmailField(max_length=200, unique=True)
    username =models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = UserManager()
    
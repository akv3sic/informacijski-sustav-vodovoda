from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.deletion import CASCADE
from ulice.models import Ulica
from role.models import Rola

class MyUserManager(BaseUserManager):
    def create_user(self, email, username, userlastname,password=None):
        
        if not username or not userlastname or not email or not password:
            raise ValueError("Unesite sve podatke")
        
        
        user = self.model(
            email= self.normalize_email(email),
            username=username,
            userlastname=userlastname,


        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, userlastname,password):
        user = self.create_user(
            email= self.normalize_email(email),
            username=username,
            userlastname=userlastname, 
            password=password,


        )   
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True   
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username= models.CharField(max_length=60)
    date_joined = models.DateTimeField(verbose_name='date_joined', auto_now_add=True)
    last_login= models.DateTimeField(verbose_name='last_login', auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)
    userlastname = models.CharField(max_length=60)
    telefon = models.CharField(max_length=22, null=True, default=None)
    kucni_broj=models.PositiveIntegerField(null=True, default=None)
    ulica=models.ForeignKey(Ulica, on_delete=CASCADE, null=True, default=None)
    rola=models.ForeignKey(Rola,  on_delete=CASCADE, null=True, default=None)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=[ 'username', 'userlastname',]

    objects= MyUserManager()

    @property
    def get_ulica(self):
        if self.ulica:
            return self.ulica.ulica
        else:
            return None

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
    


    

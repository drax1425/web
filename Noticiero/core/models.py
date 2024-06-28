from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class TipoNoticas(models.Model):
    descripcion = models.CharField(max_length=40)

    def __str__(self):
        return self.descripcion



class Periodista(models.Model):
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    telefono = models.CharField(max_length=20)
    correo = models.CharField(max_length=40)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.nombre

class Noticas(models.Model):
    periodista = models.ForeignKey(Periodista, on_delete=models.CASCADE)
    titulonoticia = models.CharField(max_length=40)
    contenido = models.CharField(max_length=120)
    tipo = models.ForeignKey(TipoNoticas, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=40)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulonoticia
    




class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        # Crea un usuario normal
        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        # Crea un superusuario (administrador)
        user = self.create_user(email=email, username=username, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email



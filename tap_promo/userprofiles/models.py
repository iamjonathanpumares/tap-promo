# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

from locales.models import Localidad

TIPO_USUARIO_CHOICES = (
	('A', 'Afiliado'),
	('C', 'Consumidor'),
	('P', 'Promotor'),
)

SEXO_CHOICES = (
	('M', 'Masculino'),
	('F', 'Femenino'),
)

class CustomUserManager(BaseUserManager):
    def create_user(self, email, full_name, tipo_usuario, password=None):
        """
        Creates and saves a User with the given email, full name and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
            tipo_usuario=tipo_usuario
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, tipo_usuario, password):
        """
        Creates and saves a superuser with the given email, full name and password.
        """
        user = self.create_user(email,
            password=password,
            full_name=full_name,
            tipo_usuario=tipo_usuario
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    full_name = models.CharField('Nombre completo', max_length=80)
    tipo_usuario = models.CharField('Tipo de usuario', max_length=1, choices=TIPO_USUARIO_CHOICES)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'tipo_usuario']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        # Simplest possible answer: All admins are staff
        return self.is_admin

class Afiliado(models.Model):
	user = models.OneToOneField(CustomUser, related_name='perfil_afiliado')
	telefono = models.CharField('Telefono', max_length=15)

	def __unicode__(self):
		return self.user.full_name

class Consumidor(models.Model):
	user = models.OneToOneField(CustomUser, related_name='perfil_consumidor')
	localidad = models.ForeignKey(Localidad, related_name='consumidores')
	nombre = models.CharField('Nombre', max_length=80)
	apellidos = models.CharField('Apellidos', max_length=150)
	fecha_nacimiento = models.DateField('Fecha nacimiento')
	imagen = models.ImageField('Imagen', upload_to='userprofiles/consumidores')
	sexo = models.CharField('Sexo', max_length=1, choices=SEXO_CHOICES)
	fecha_registro = models.DateTimeField('Fecha de registro', auto_now_add=True)

	def __unicode__(self):
		return self.user.full_name

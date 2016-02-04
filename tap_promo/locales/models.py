# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from empresas.models import Empresa

class Local(models.Model):
	empresa = models.ForeignKey(Empresa, related_name='locales')
	direccion = models.CharField('Dirección', max_length=150)
	telefono = models.CharField('Telefono', max_length=15, blank=True)
	email = models.EmailField('Email')
	latitud = models.FloatField('Latitud')
	longitud = models.FloatField('Longitud')
	pais = models.CharField('País', max_length=150)
	estado = models.CharField('Estado', max_length=150)
	localidad = models.CharField('Localidad', max_length=150)
	is_matriz = models.BooleanField()
	imagen_local = models.ImageField(upload_to='userprofiles/locales', verbose_name='Imagen del local', blank=True, null=True)
	ssid = models.CharField('SSID', max_length=35)
	ssid_pass = models.CharField('Password del SSID', max_length=35)

	def __unicode__(self):
		return self.empresa.nombre_empresa + " - " + self.direccion

class Pais(models.Model):
	nombre = models.CharField('Nombre del país', max_length=150)

class Estado(models.Model):
	pais = models.ForeignKey(Pais, related_name='estados')
	nombre = models.CharField('Nombre del estado', max_length=150)

class Localidad(models.Model):
	estado = models.ForeignKey(Estado, related_name='localidades')
	nombre = models.CharField('Nombre de la localidad', max_length=150)

# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from userprofiles.models import Afiliado

ESTATUS_CHOICES = (
	('A', 'Activo'),
	('I', 'Inactivo'),
	('P', 'Pendiente'),
	('B', 'Bloqueado'),
)

class Empresa(models.Model):
	afiliado = models.ForeignKey(Afiliado, related_name='empresas')
	giros = models.ManyToManyField('Giro', related_name='empresas')
	nombre_empresa = models.CharField(max_length=255, verbose_name='Empresa')
	descripcion = models.TextField('Descripción', blank=True)
	estatus = models.CharField('Estatus', max_length=1, choices=ESTATUS_CHOICES, default='P')
	web = models.URLField('Web', blank=True)
	facebook = models.URLField('Facebook', blank=True)
	twitter = models.URLField('Twitter', blank=True)
	instagram = models.URLField('Instagram', blank=True)
	youtube = models.URLField('Youtube', blank=True)
	codigo_validacion = models.CharField('Codigo validación', max_length=100)
	logo = models.ImageField('Logo', upload_to='userprofiles/logos', blank=True, null=True)

	def __unicode__(self):
		return self.nombre_empresa

class Giro(models.Model):
	giro = models.CharField('Giro o actividad de la empresa', max_length=100)

	def __unicode__(self):
		return self.giro

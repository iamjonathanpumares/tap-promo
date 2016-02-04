from django.contrib import admin

from .models import Empresa, Giro, Local

admin.site.register(Empresa)
admin.site.register(Giro)
admin.site.register(Local)

from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(TipoNoticas)
admin.site.register(Periodista)
admin.site.register(Noticas)
admin.site.register(CustomUser)
from django.contrib import admin

from . import models


class KlientasAdmin(admin.ModelAdmin):
    list_display = ('kliento_vardas', 'kliento_pavarde',)


admin.site.register(models.Klientas, KlientasAdmin)
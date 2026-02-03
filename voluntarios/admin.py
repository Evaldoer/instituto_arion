from django.contrib import admin
from .models import Voluntario

@admin.register(Voluntario)
class VoluntarioAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "area", "criado_em")
    search_fields = ("nome", "email", "area")
    list_filter = ("area", "criado_em")
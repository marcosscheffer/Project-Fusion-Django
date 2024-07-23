from django.contrib import admin
from .models import Position, Services, Team, Features


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("created_at", "title", "is_active")
    

@admin.register(Services)
class Service(admin.ModelAdmin):
    list_display = ("created_at", "updated_at", "service",
                    "icon", 'is_active')
    

@admin.register(Team)
class Team(admin.ModelAdmin):
    list_display = ("created_at", "updated_at", "name",
                    "position", "is_active")
    

@admin.register(Features)
class Features(admin.ModelAdmin):
    list_display = ("created_at", "title", "icon", 'is_active')

from django.contrib import admin
from .models import GoodDeed

@admin.register(GoodDeed)
class GoodDeedAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')

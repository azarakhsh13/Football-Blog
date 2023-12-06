from django.contrib import admin
from .models import Coach, Player


# Register your models here.
class PlayerAdmin(admin.ModelAdmin):
    list_filter = ('playing_history', 'age')
    list_display = ('first_name', 'last_name', 'national_id', 'age', 'playing_history')


class CoachAdmin(admin.ModelAdmin):
    list_filter = ('certificate', 'professional_history')
    list_display = ('first_name', 'last_name', 'national_id', 'age', 'professional_history')


admin.site.register(Coach, CoachAdmin)
admin.site.register(Player, PlayerAdmin)

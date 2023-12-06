from django.contrib import admin
from .models import Author, Post, Player, Coach


# Register your models here

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('date', 'last_modified')
    list_display = ('writers_name', 'visibility', 'date', 'last_modified')
    list_filter = ('date', 'visibility')

    @admin.display(description="Authors")
    def writers_name(self, obj):
        writers = obj.author.all()
        names = ''
        for writer in writers:
            names += writer.__str__() + ', '
        return f'{names}'


class PlayerAdmin(admin.ModelAdmin):
    list_filter = ('playing_history', 'age')
    list_display = ('first_name', 'last_name', 'national_id', 'age', 'playing_history')


class CoachAdmin(admin.ModelAdmin):
    list_filter = ('certificate', 'professional_history')
    list_display = ('first_name', 'last_name', 'national_id', 'age', 'professional_history')


admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Coach, CoachAdmin)
admin.site.register(Player, PlayerAdmin)

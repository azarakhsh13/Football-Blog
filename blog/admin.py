from django.contrib import admin
from .models import Author, Post


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


admin.site.register(Author)
admin.site.register(Post, PostAdmin)

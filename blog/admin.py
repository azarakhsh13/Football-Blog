from django.contrib import admin
from .models import Author, Post


# Register your models here

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)


admin.site.register(Author)
admin.site.register(Post, PostAdmin)

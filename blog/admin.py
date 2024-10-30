from django.contrib import admin

from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha')  
    search_fields = ('titulo', 'autor')
    list_filter = ('fecha',)

admin.site.register(Blog, BlogAdmin)

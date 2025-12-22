from django.contrib import admin
from .models import Genre, CollectionItem

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(CollectionItem)
class CollectionItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created_at')
    list_filter = ('genres',)
    search_fields = ('title', 'description')
    filter_horizontal = ('genres',)

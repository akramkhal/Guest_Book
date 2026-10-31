from django.contrib import admin
from webapp.models import Guest


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('id', 'author_name', 'author_email', 'status', 'text', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at', 'updated_at')
    search_fields = ('author_name', 'author_email')


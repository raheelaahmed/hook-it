from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    # You can customize the admin interface for the Contact model here
    list_display = ('email', 'subject', 'message')

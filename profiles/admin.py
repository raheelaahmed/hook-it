from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'default_phone_number', 'default_country', 'default_town_or_city')  # Add other fields you want to display
    search_fields = ['user__username', 'default_phone_number', 'default_country']  # You can also search by related fields

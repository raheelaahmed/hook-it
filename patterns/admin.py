from django.contrib import admin
from .models import Category, Pattern, Review
from django_ckeditor_5.widgets import CKEditor5Widget
from django_ckeditor_5.fields import CKEditor5Field 
from django import forms


# Register your models here.

admin.site.register(Category)



# Custom form for the Pattern model
class PatternAdminForm(forms.ModelForm):
    class Meta:
        model = Pattern
        fields = '__all__'

    # Attach the CKEditor5Widget to the 'description' field in the admin
    description = forms.CharField(widget=CKEditor5Widget())

# Custom admin class for Pattern model
class PatternAdmin(admin.ModelAdmin):
    form = PatternAdminForm
    list_display = ('name', 'price', 'category', 'difficulty', 'rating', 'date_created')
    search_fields = ('name', 'category__name')
    list_filter = ('category', 'difficulty', 'date_created')

# Register the Pattern model with the custom admin
admin.site.register(Pattern, PatternAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['pattern', 'user', 'rating', 'created_at']
    search_fields = ['pattern__name', 'user__username']

admin.site.register(Review, ReviewAdmin)

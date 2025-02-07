from django import forms
from .models import Pattern, Category
from django_ckeditor_5.widgets import CKEditor5Widget  # Use CKEditor5Widget if you are using CKEditor 5

class PatternForm(forms.ModelForm):

    class Meta:
        model = Pattern
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Fetch all categories from the database
        categories = Category.objects.all()
        
        # Create a list of tuples with the category id and name for the 'category' field choices
        category_choices = [(category.id, category.name) for category in categories]

        # Set the category field choices to the names
        self.fields['category'].choices = category_choices

        # Apply default styling to all form fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control border-black rounded-0'

        # Optionally, you can customize the widgets for file fields (e.g., pattern or image)
        self.fields['pattern'].widget.attrs.update({'class': 'form-control-file'})
        self.fields['image'].widget.attrs.update({'class': 'form-control-file'})

        # Apply CKEditor widget to the 'description' field
        self.fields['description'].widget = CKEditor5Widget(config_name='default')  # Add CKEditor widget

from django import forms
from .models import Pattern, Category
from .widgets import CustomClearableFileInput

class PatternForm(forms.ModelForm):

    class Meta:
        model = Pattern
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Fetch all categories from the database
        categories = Category.objects.all()

        # Create a list of tuples with category id and name
        category_choices = [(category.id, category.name) for category in categories]

        # Set the 'category' field choices to the list of tuples
        self.fields['category'].choices = category_choices

        # Apply default styling to all form fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

        # Define image field with custom widget (if needed)
        self.fields['image'] = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)



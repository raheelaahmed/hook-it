from django import forms
from .models import Order
from crispy_forms.helper import FormHelper


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name',
                  'email',
                  'phone_number',
                  'postcode',
                  'town_or_city',
                  'street_address1',
                  'street_address2',
                  'county',
                  'country')
        labels = {
            'country': 'Country',
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            if field != 'country':
                self.fields[field].label = False

        # Add CSS classes to the form and its container
        self.helper = FormHelper()
        self.helper.form_class = 'form-group'
        self.helper.label_class = 'col-form-label'
        self.helper.field_class = 'col-form-input'

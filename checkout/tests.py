from django.test import TestCase
from django.urls import reverse

from django.contrib.auth import get_user_model
from patterns.models import Pattern
from .forms import OrderForm


class CheckoutTestCase(TestCase):

    def setUp(self):
        # Create a user for authenticated requests
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='password123'
        )

        # Create a pattern for testing
        self.pattern = Pattern.objects.create(
            name='Test Pattern',
            description='A sample test pattern',
            price=10.0
        )

        # Simulate adding pattern to the shopping bag
        self.session = self.client.session
        self.session['bag'] = {
            str(self.pattern.id): 1  # Adding one item to the bag
        }
        self.session.save()

    def test_checkout_page_loads(self):
        """Test if the checkout page loads correctly."""
        response = self.client.get(reverse('checkout'))  # Check the checkout URL
        self.assertEqual(response.status_code, 200)


class OrderFormTest(TestCase):
    def test_valid_order_form(self):
        """Test OrderForm with valid data."""
        form_data = {
            'full_name': 'John Doe',
            'email': 'john@example.com',
            'phone_number': '1234567890',
            'postcode': '12345',
            'town_or_city': 'Test City',
            'street_address1': '123 Main St',
            'street_address2': 'Apt 1',
            'county': 'Test County',
            'country': 'US',
        }
        form = OrderForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)  # Check if form is valid

    def test_invalid_order_form_missing_fields(self):
        """Test OrderForm with missing required fields."""
        form_data = {
            'full_name': '',
            'email': '',
            'phone_number': '',
            'postcode': '',
            'town_or_city': '',
            'street_address1': '',
            'street_address2': '',
            'county': '',
            'country': '',
        }
        form = OrderForm(data=form_data)
        self.assertFalse(form.is_valid())  # Form should be invalid
        self.assertIn('full_name', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('phone_number', form.errors)

    def test_invalid_order_form_invalid_email(self):
        """Test OrderForm with an invalid email."""
        form_data = {
            'full_name': 'John Doe',
            'email': 'invalid-email',  # Invalid email format
            'phone_number': '1234567890',
            'postcode': '12345',
            'town_or_city': 'Test City',
            'street_address1': '123 Main St',
            'street_address2': 'Apt 1',
            'county': 'Test County',
            'country': 'US',
        }
        form = OrderForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_optional_fields(self):
        """Test OrderForm with only required fields filled."""
        form_data = {
            'full_name': 'Jane Doe',
            'email': 'jane@example.com',
            'phone_number': '9876543210',
            'postcode': '54321',
            'town_or_city': 'Sample City',
            'street_address1': '456 Sample St',
            'county': 'Sample County',
            'country': 'CA',
        }
        form = OrderForm(data=form_data)
        self.assertTrue(form.is_valid())  # Form should be valid even with optional fields missing

from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.messages import get_messages
from .models import UserProfile
from checkout.models import Order, OrderLineItem
from patterns.models import Pattern  # Assuming patterns exist
from django.core.files.uploadedfile import SimpleUploadedFile


class ProfileViewTest(TestCase):
    """Tests for the profile views."""

    def setUp(self):
        """Set up test user, profile, and order data."""
        self.user = User.objects.create_user(
            username="testuser", password="testpass"
        )
        self.profile = UserProfile.objects.get(user=self.user)

        self.pattern = Pattern.objects.create(
            name="Test Pattern",
            description="Test description",
            price=10.00,
            pattern=SimpleUploadedFile(
                "test.pdf", b"file_content", content_type="application/pdf"
            ),
        )

        self.order = Order.objects.create(
            order_number="123456",
            user_profile=self.profile,
            full_name="John Doe",
            email="test@example.com",
            phone_number="1234567890",
            country="US",
            postcode="12345",
            town_or_city="Test City",
            street_address1="123 Test St",
            street_address2="Apt 1",
            county="Test County",
        )

        self.order_line_item = OrderLineItem.objects.create(
            order=self.order, pattern=self.pattern, quantity=1
        )

    def test_profile_page_requires_login(self):
        """Ensure login is required to access profile."""
        response = self.client.get(reverse("profile"))
        self.assertNotEqual(response.status_code, 200)  # Should be redirected

    def test_profile_page_loads_correctly(self):
        """Ensure profile page loads for logged-in users."""
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse("profile"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")

    def test_profile_update_success(self):
        """Ensure profile updates successfully with valid data."""
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(
            reverse("profile"),
            {
                "default_phone_number": "9876543210",
                "default_street_address1": "New Address",
                "default_street_address2": "",
                "default_town_or_city": "New City",
                "default_postcode": "67890",
                "default_county": "New County",
                "default_country": "US",
            },
        )
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.default_phone_number, "9876543210")
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn("Profile updated successfully", messages)

    def test_order_history_access(self):
        """Ensure users can access their order history."""
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(
            reverse("order_history", args=[self.order.order_number])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "checkout/checkout_success.html")

    def test_order_history_contains_patterns(self):
        """Ensure order history includes
        pattern download links if available."""
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(
            reverse("order_history", args=[self.order.order_number])
        )
        self.assertContains(response, self.pattern.name)
        self.assertContains(response, self.pattern.pattern.url)

    def test_order_history_nonexistent_order(self):
        """Ensure accessing a nonexistent order history page returns 404."""
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse("order_history", args=["999999"]))
        self.assertEqual(response.status_code, 404)

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from patterns.models import Pattern


class BagViewTest(TestCase):

    def setUp(self):
        """ Set up a pattern and a user to test with. """
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Create a test pattern to add to the bag
        self.pattern = Pattern.objects.create(
            name="Test Pattern",
            description="This is a test pattern.",
            price=10.00,
        )
        # Log in as the test user
        self.client.login(username='testuser', password='testpassword')

    def test_remove_from_bag(self):
        """ Test that an item is removed from the bag. """
        # First, add the pattern to the shopping bag
        self.client.post(reverse('add_to_bag', args=[self.pattern.pk]), {'quantity': 1})

        # Check if the item is in the bag
        bag = self.client.session.get('bag', {})
        self.assertIn(str(self.pattern.pk), bag)  # Item should be in the bag
        # Remove the item from the bag
        response = self.client.post(reverse('remove_from_bag', args=[self.pattern.pk]))
        # Check if the item is removed from the bag
        bag = self.client.session.get('bag', {})
        self.assertNotIn(str(self.pattern.pk), bag)  # Item should no longer be in the bag
        # Check that the user is redirected to the view_bag page
        self.assertRedirects(response, reverse('view_bag'))

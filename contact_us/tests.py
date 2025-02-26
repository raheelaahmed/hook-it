from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from django.core import mail


class ContactViewTest(TestCase):
    """"Testing contact us"""

    def test_contact_view_post_valid_data(self):
        """Test that a valid form submission sends the email and shows a success message."""
        # Define the valid form data
        form_data = {
            'subject': 'Test Subject',
            'email': 'testuser@example.com',
            'message': 'This is a test message.',
        }

        # Simulate a POST request with the valid form data
        response = self.client.post(reverse('contact'), form_data)

        # Check if the response is a redirect (302)
        self.assertEqual(response.status_code, 302)

        # Check if the email was sent
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Test Subject')
        self.assertEqual(mail.outbox[0].body, 'This is a test message.')
        self.assertEqual(mail.outbox[0].from_email, 'testuser@example.com')

        # Check if the success message is present in the messages
        messages = [msg.message for msg in get_messages(response.wsgi_request)]
        self.assertIn("Your message has been sent successfully!", messages)

    def test_contact_view_get(self):
        """Test that the contact form is displayed correctly for GET requests."""
        response = self.client.get(reverse('contact'))

        # Check if the response is 200 OK
        self.assertEqual(response.status_code, 200)

        # Check if the contact form is rendered
        self.assertTemplateUsed(response, 'contact_us/contact.html')

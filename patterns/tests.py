from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Pattern, Review


class PatternViewTest(TestCase):
    """Tests for the Pattern views: add, edit, and delete (Superuser only)."""

    def setUp(self):
        """Create test users and a pattern with a mock image."""
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass"
        )
        self.superuser = User.objects.create_superuser(
            username="admin",
            password="adminpass"
        )

        self.image = SimpleUploadedFile(
            "test.jpg",
            b"file_content",
            content_type="image/jpeg"
        )

        self.pattern = Pattern.objects.create(
            name="Test Pattern",
            description="This is a test pattern.",
            price=9.99,
            date_created=timezone.now(),
            image=self.image,
        )

    def test_add_pattern_superuser(self):
        """Ensure only superusers can access the add pattern page."""
        self.client.login(username="admin", password="adminpass")
        response = self.client.get(reverse('add_pattern'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'patterns/add_pattern.html')

    def test_add_pattern_non_superuser(self):
        """Ensure non-superusers cannot access the add pattern page."""
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse('add_pattern'))
        self.assertNotEqual(response.status_code, 200)  # Should be redirected

    def test_edit_pattern_superuser(self):
        """Ensure only superusers can edit a pattern."""
        self.client.login(username="admin", password="adminpass")
        response = self.client.get(
            reverse('edit_pattern', args=[self.pattern.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'patterns/edit_pattern.html')

    def test_edit_pattern_non_superuser(self):
        """Ensure non-superusers cannot edit a pattern."""
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(
            reverse('edit_pattern', args=[self.pattern.pk])
        )
        self.assertNotEqual(response.status_code, 200)

    def test_delete_pattern_superuser(self):
        """Ensure only superusers can delete a pattern."""
        self.client.login(username="admin", password="adminpass")
        response = self.client.post(
            reverse('delete_pattern', args=[self.pattern.pk])
        )
        self.assertEqual(response.status_code, 302)

    def test_delete_pattern_non_superuser(self):
        """Ensure non-superusers cannot delete a pattern."""
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(
            reverse('delete_pattern', args=[self.pattern.pk])
        )
        self.assertNotEqual(response.status_code, 200)


class ReviewViewTest(TestCase):
    """Tests for the Review views: edit and delete
    (Superuser and review owner only)."""

    def setUp(self):
        """Create test users, a pattern, and a review."""
        self.user = User.objects.create_user(
            username="testuser", password="testpass"
        )
        self.other_user = User.objects.create_user(
            username="otheruser", password="otherpass"
        )
        self.superuser = User.objects.create_superuser(
            username="admin", password="adminpass"
        )

        self.image = SimpleUploadedFile(
            "test.jpg", b"file_content", content_type="image/jpeg"
        )

        self.pattern = Pattern.objects.create(
            name="Test Pattern",
            description="This is a test pattern.",
            price=9.99,
            image=self.image,
        )

        self.review = Review.objects.create(
            pattern=self.pattern,
            user=self.user,
            rating=5,
            comment="Great pattern!",
        )

    def test_edit_review_owner(self):
        """Ensure the user who created the review can edit it."""
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(
            reverse('edit-review', args=[self.review.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'patterns/edit_review.html')

    def test_edit_review_superuser(self):
        """Ensure a superuser can edit any review."""
        self.client.login(username="admin", password="adminpass")
        response = self.client.get(
            reverse('edit-review', args=[self.review.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'patterns/edit_review.html')

    def test_edit_review_other_user(self):
        """Ensure another user
         (who did not create the review) cannot edit it."""
        self.client.login(username="otheruser", password="otherpass")
        response = self.client.get(
            reverse('edit-review', args=[self.review.pk])
        )
        self.assertNotEqual(response.status_code, 200)

    def test_delete_review_owner(self):
        """Ensure the user who created the review can delete it."""
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(
            reverse('delete-review', args=[self.pattern.pk, self.review.pk])
        )
        self.assertEqual(response.status_code, 302)

    def test_delete_review_superuser(self):
        """Ensure a superuser can delete any review."""
        self.client.login(username="admin", password="adminpass")
        response = self.client.post(
            reverse('delete-review', args=[self.pattern.pk, self.review.pk])
        )
        self.assertEqual(response.status_code, 302)

    def test_delete_review_other_user(self):
        """Ensure another user
        (who did not create the review) cannot delete it."""
        self.client.login(username="otheruser", password="otherpass")
        response = self.client.post(
            reverse('delete-review', args=[self.pattern.pk, self.review.pk])
        )
        self.assertNotEqual(response.status_code, 200)

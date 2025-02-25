from django.db import models
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


# Pattern model
class Pattern(models.Model):
    DIFFICULTY_LEVEL = (
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced')
    )

    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    difficulty = models.CharField(
        choices=DIFFICULTY_LEVEL,
        max_length=254,
        null=True,
        blank=True
    )
    name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date_created = models.DateTimeField(default=timezone.now)
    image = models.ImageField(null=True, blank=True)
    pattern = models.FileField(upload_to='media/files', null=True, blank=True)
    rating = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )
    description = CKEditor5Field(null=True, blank=True)

    def __str__(self):
        return self.name


# Review model
class Review(models.Model):
    pattern = models.ForeignKey(
        'Pattern',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='reviews'
    )
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        choices=[(i, i) for i in range(1, 6)],
        default=5
    )  # Rating scale from 1 to 5 stars
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return (
            f"Review for {self.pattern.name} by "
            f"{self.user.username if self.user else 'Anonymous'}"
        )

    class Meta:
        ordering = ['-created_at']  # Show most recent reviews first

from django.db import models
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field 


class Category(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

class Pattern(models.Model):
    
    DIFFICULTY_LEVEL = (
        ('Beginner', 'Beginner'),  
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced')
    )

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
    )
    difficulty = models.CharField( 
        choices=DIFFICULTY_LEVEL, max_length=254, null=True, blank=True
    )

    name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date_created = models.DateTimeField(default=timezone.now)
    image = models.ImageField(null=True, blank=True)
    pattern = models.FileField(upload_to='media/files', null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    description = CKEditor5Field(null=True, blank=True)                       

    def __str__(self):
        return self.name
   
  
from django.urls import path
from . import views

urlpatterns = [
      path('', views.all_patterns, name='patterns'),  # Empty path means the home page for patterns

    # View the detail of a specific pattern
    path('pattern/<int:pattern_id>/', views.pattern_detail, name='pattern-detail'),

    # Add a review for a specific pattern
    path('pattern/<int:pattern_id>/review/', views.add_review, name='add_review'),
    path('add/', views.add_pattern, name='add_pattern'),
   
]
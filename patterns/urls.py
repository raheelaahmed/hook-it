from django.urls import path
from . import views

urlpatterns = [
      path('', views.all_patterns, name='patterns'),
      path('<int:pattern_id>/', views.pattern_detail, name='pattern-detail'),
      path('<int:pattern_id>/add-review/', views.add_review, name='add-review'),
      path('review/edit/<int:review_id>/', views.edit_review, name='edit-review'),
      path('<int:pattern_id>/review/<int:review_id>/delete/', views.delete_review, name='delete-review'),
      path('add/', views.add_pattern, name='add_pattern'),
      path('edit/<int:pattern_id>/', views.edit_pattern, name='edit_pattern'),
      path('delete_pattern/<int:pattern_id>/', views.delete_pattern, name='delete_pattern'),

]

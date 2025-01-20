from django.urls import path
from . import views

urlpatterns = [
     path(' ', views.all_patterns, name='patterns'),
     path('<pattern_id>', views.pattern_detail, name='pattern-detail'),
   
]
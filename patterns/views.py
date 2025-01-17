from django.shortcuts import render
from .models import Pattern  

def all_patterns(request):
    """ A view to return all patterns """

    
    patterns = Pattern.objects.all()

    
    context = {'patterns': patterns}

    
    return render(request, 'patterns/pattern.html', context)
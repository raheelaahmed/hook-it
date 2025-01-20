from django.shortcuts import render, get_object_or_404
from .models import Pattern  

def all_patterns(request):
    """ A view to return all patterns """

    
    patterns = Pattern.objects.all()
    currency_symbol = "€" 

    
    context = {
        
    'patterns': patterns,
    'currency_symbol': currency_symbol,
    }

    
    return render(request, 'patterns/pattern.html', context)

# pattern detail view 
def pattern_detail(request, pattern_id):
    """ A view to show individual pattern detail """

    # Fetch the Pattern object or return a 404 if not found
    pattern = get_object_or_404(Pattern, pk=pattern_id)
    currency_symbol = "€" 

    # Context to pass to the template
    context = {
        'pattern': pattern,
        'currency_symbol': currency_symbol,
    }

    # Render the pattern_detail.html template with the context
    return render(request, 'patterns/pattern_detail.html', context)

  

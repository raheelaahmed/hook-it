from django.shortcuts import render, get_object_or_404
from .models import Pattern  
from django.contrib import messages
from django.db.models import Q
from django.urls import reverse

from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from django.urls import reverse
from .models import Pattern  

def all_patterns(request):
    """ A view to return all patterns including queries and search """


    patterns = Pattern.objects.all()
    currency_symbol = "€"
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            
            
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('patterns'))
            
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            patterns = patterns.filter(queries)

                        
            if not patterns.exists():
                messages.error(request, "No patterns found for your search criteria.")

    context = {
        'patterns': patterns,
        'currency_symbol': currency_symbol,
        'search_term': query,
    }

    return render(request, 'patterns/pattern.html', context)


# pattern detail view 
def pattern_detail(request, pattern_id):
    """ A view to show individual pattern detail """

    
    pattern = get_object_or_404(Pattern, pk=pattern_id)
    currency_symbol = "€" 

    
    context = {
        'pattern': pattern,
        'currency_symbol': currency_symbol,
    }

    
    return render(request, 'patterns/pattern_detail.html', context)

  

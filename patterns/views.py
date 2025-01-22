from django.shortcuts import render, get_object_or_404
from .models import Pattern, Category 
from django.contrib import messages
from django.db.models import Q
from django.urls import reverse


def all_patterns(request):
    """ A view to return all patterns including queries and search """
    patterns = Pattern.objects.all()
    currency_symbol = "€"
    query = None

    # Get the combined sorting and direction
    sort_by = request.GET.get('sort_by', 'date_created_asc')  # Default sort is 'date_created_asc'

    # Extract sort field and direction
    try:
        sort_field, direction = sort_by.split('_')  # Split by underscore
    except ValueError:
        # Handle the case where 'sort_by' is not in the correct format
        sort_field, direction = 'date_created', 'asc'  # Default sorting if not correct

    # Handle search query
    if 'q' in request.GET:
        query = request.GET['q']
        
        if not query:
            messages.error(request, "You didn't enter any search criteria!")
            return redirect('patterns')

        # Construct queries for pattern name, description, category name, and difficulty
        queries = Q(name__icontains=query) | Q(description__icontains=query)
        queries |= Q(category__name__icontains=query)
        queries |= Q(difficulty__icontains=query)
        patterns = patterns.filter(queries)

        if not patterns.exists():
            messages.error(request, "No patterns found for your search criteria.")

    # Sorting logic: Apply sort_by and direction
    if sort_field == 'name':
        sortkey = 'name'
    elif sort_field == 'price':
        sortkey = 'price'
    elif sort_field == 'difficulty':
        sortkey = 'difficulty'
    elif sort_field == 'date_created':
        sortkey = 'date_created'
    else:
        sortkey = 'date_created'  # Default sorting if not specified

    # Apply ascending or descending order based on the direction
    if direction == 'desc':
        sortkey = f'-{sortkey}'  # Prepend '-' for descending order

    patterns = patterns.order_by(sortkey)

    # Prepare context for the template
    context = {
        'patterns': patterns,
        'currency_symbol': currency_symbol,
        'search_term': query,
        'sort_by': sort_by,  # Pass the combined sort_by for template to remember
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

  

  

  

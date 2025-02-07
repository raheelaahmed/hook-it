from django.shortcuts import render, get_object_or_404,redirect,reverse
from .models import Pattern, Review
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import PatternForm

def all_patterns(request):
    """ A view to return all patterns including queries and search """
    patterns = Pattern.objects.all()
    currency_symbol = "€"
    query = None

    # Sorting logic
    sort_by = request.GET.get('sort_by', 'date_created_asc')  # Default sorting
    try:
        sort_field, direction = sort_by.split('_')  # 'field_direction' format
    except ValueError:
        sort_field, direction = 'date_created', 'asc'  # Default to 'date_created' with ascending order

    # Handle sorting based on the selected field
    if sort_field == 'name':
        sortkey = 'name'
    elif sort_field == 'price':
        sortkey = 'price'
    elif sort_field == 'difficulty':
        sortkey = 'difficulty'
    elif sort_field == 'date_created':  # Handle sorting by date_created
        sortkey = 'date_created'

    # Apply the sorting direction (ascending or descending)
    if direction == 'desc':
        sortkey = f'-{sortkey}'  # Reverse the order for descending (Newest)

    # Apply sorting to the patterns
    patterns = patterns.order_by(sortkey)

    # Search functionality
    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(request, "You didn't enter any search criteria!")
            return redirect('patterns')

        queries = Q(name__icontains=query) | Q(description__icontains=query) | \
                 Q(category__name__icontains=query) | Q(difficulty__icontains=query)
        patterns = patterns.filter(queries)

        if not patterns.exists():
            messages.error(request, "No patterns found for your search criteria.")

    # Pagination
    paginator = Paginator(patterns, 9)  # Show 9 patterns per page
    page_number = request.GET.get('page')
    pattern_list = paginator.get_page(page_number)

    context = { 
        'pattern_list': pattern_list, 
        'currency_symbol': currency_symbol,
        'search_term': query,
        'sort_by': sort_by,  # Pass sorting option back to template
    }

    return render(request, 'patterns/pattern.html', context) 




# pattern detail view 


def pattern_detail(request, pattern_id):
    """ A view to show individual pattern detail """
    pattern = get_object_or_404(Pattern, pk=pattern_id)
    reviews = pattern.reviews.all() 
    currency_symbol = "€" 
    context = {
        'pattern': pattern,
        'currency_symbol': currency_symbol,
        'reviews': reviews, 
    }

    return render(request, 'patterns/pattern_detail.html', context)


# review

def add_review(request, pattern_id):
    """ A view to handle adding a review to a pattern """

    # Get the pattern object
    pattern = get_object_or_404(Pattern, pk=pattern_id)

    if request.method == 'POST':
        # Get the rating and comment from the POST request
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        # Validation for rating and comment
        if not rating or not comment:
            messages.error(request, "Both rating and comment are required.")
            return redirect('pattern-detail', pattern_id=pattern.id)  # Correct redirection here

        try:
            rating = int(rating)  # Ensure rating is an integer
            if not (1 <= rating <= 5):
                raise ValueError("Rating must be between 1 and 5.")
        except ValueError:
            messages.error(request, "Invalid rating value. It must be between 1 and 5.")
            return redirect('pattern-detail', pattern_id=pattern.id)  # Correct redirection here

        # Create and save the review
        review = Review(
            pattern=pattern,
            user=request.user,  # Automatically associate review with logged-in user
            rating=rating,
            comment=comment
        )
        review.save()

        # Redirect to the pattern detail page after the review is saved
        messages.success(request, "Your review has been added successfully!")
        return redirect('pattern-detail', pattern_id=pattern.id)  # Correct redirection here

    # If method is not POST, return a 405 error
    return HttpResponse("Invalid method", status=405)


def add_pattern(request):
    """ Add a pattern to the store """
    if request.method == 'POST':
        form = PatternForm(request.POST, request.FILES)
        if form.is_valid():
            pattern = form.save()
            messages.success(request, 'Successfully added pattern!')
            return redirect(reverse('pattern_detail', args=[pattern.id]))
        else:
            messages.error(request, 'Failed to add pattern. Please ensure the form is valid.')
    else:

        form = PatternForm()
        
        template = 'patterns/add_pattern.html'
        context = {
            'form': form,
        }

    return render(request, template, context)


def edit_pattern(request, pattern_id):
    """ Edit a pattern in the store """
    pattern = get_object_or_404(Pattern, pk=pattern_id)
    if request.method == 'POST':
        form = PatternForm(request.POST, request.FILES, instance=pattern)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated pattern!')
            return redirect(reverse('pattern_detail', args=[pattern.id]))
        else:
            messages.error(request, 'Failed to update pattern. Please ensure the form is valid.')
    else:
        form = PatternForm(instance=pattern)
        messages.info(request, f'You are editing {pattern.name}')

    template = 'patterns/edit_pattern.html'
    context = {
        'form': form,
        'pattern': pattern,
    }

    return render(request, template, context)


def delete_pattern(request, pattern_id):
    """ Delete a pattern from the store """
    pattern = get_object_or_404(Pattern, pk=pattern_id)
    pattern.delete()
    messages.success(request, 'Pattern deleted!')
    return redirect(reverse('patterns'))


  

  

  

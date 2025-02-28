from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.conf import settings

from .models import Pattern, Review
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
        sort_field, direction = 'date_created', 'asc'  # Default order

    # Sorting mapping
    sort_options = {
        'name': 'name',
        'price': 'price',
        'difficulty': 'difficulty',
        'date_created': 'date_created',
    }
    sortkey = sort_options.get(sort_field, 'date_created')

    if direction == 'desc':
        sortkey = f'-{sortkey}'  # Reverse order for descending

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
        'sort_by': sort_by,
    }

    return render(request, 'patterns/pattern.html', context)


def pattern_detail(request, pattern_id):
    """ A view to show individual pattern detail """
    pattern = get_object_or_404(Pattern, pk=pattern_id)
    reviews = pattern.reviews.all()
    currency_symbol = "€"

    context = {
        'pattern': pattern,
        'currency_symbol': currency_symbol,
        'reviews': reviews,
        'MEDIA_URL': settings.MEDIA_URL
    }

    return render(request, 'patterns/pattern_detail.html', context)


def add_review(request, pattern_id):
    """ A view to handle adding a review to a pattern """
    pattern = get_object_or_404(Pattern, pk=pattern_id)

    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        if not rating or not comment:
            messages.error(request, "Both rating and comment are required.")
            return redirect('pattern-detail', pattern_id=pattern.id)

        try:
            rating = int(rating)
            if not (1 <= rating <= 5):
                raise ValueError("Rating must be between 1 and 5.")
        except ValueError:
            messages.error(request, "Invalid rating value. It must be between 1 and 5.")
            return redirect('pattern-detail', pattern_id=pattern.id)

        Review.objects.create(
            pattern=pattern,
            user=request.user,
            rating=rating,
            comment=comment
        )

        messages.success(request, "Your review has been added successfully!")
        return redirect('pattern-detail', pattern_id=pattern.id)


@login_required
def edit_review(request, review_id):
    """ A view to handle editing a review """
    review = get_object_or_404(Review, id=review_id)

    if review.user != request.user and not request.user.is_superuser:
        messages.error(request, "You do not have permission to edit this review.")
        return redirect('pattern-detail', pattern_id=review.pattern.id)

    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        if not rating or not comment:
            messages.error(request, "Both rating and comment are required.")
            return redirect('edit-review', review_id=review.id)

        try:
            rating = int(rating)
            if not (1 <= rating <= 5):
                raise ValueError("Rating must be between 1 and 5.")
        except ValueError:
            messages.error(request, "Invalid rating value. It must be between 1 and 5.")
            return redirect('edit-review', review_id=review.id)

        review.rating = rating
        review.comment = comment
        review.save()

        messages.success(request, "Your review has been updated successfully!")
        return redirect('pattern-detail', pattern_id=review.pattern.id)

    return render(request, 'patterns/edit_review.html', {'review': review})


@login_required
def delete_review(request, pattern_id, review_id):
    """ Delete a review for a pattern """
    review = get_object_or_404(Review, id=review_id, pattern_id=pattern_id)

    if review.user != request.user and not request.user.is_superuser:
        messages.error(request, 'You do not have permission to delete this review.')
        return redirect('pattern-detail', pattern_id=pattern_id)

    review.delete()
    messages.success(request, 'Review deleted successfully!')
    return redirect('pattern-detail', pattern_id=pattern_id)


@login_required
def add_pattern(request):
    """ Add a pattern to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PatternForm(request.POST, request.FILES)
        if form.is_valid():
            pattern = form.save(commit=False)  # Get instance but don't save yet
            pattern.save()
            messages.success(request, 'Successfully added pattern!')
            return redirect('pattern-detail', pattern_id=pattern.id)
        else:
            messages.error(request, 'Failed to add pattern. Please ensure the form is valid.')
    else:
        form = PatternForm()

    return render(request, 'patterns/add_pattern.html', {
        'form': form,
        'MEDIA_URL': settings.MEDIA_URL
    })


@login_required
def edit_pattern(request, pattern_id):
    """ Edit a pattern in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    pattern = get_object_or_404(Pattern, pk=pattern_id)

    if request.method == 'POST':
        form = PatternForm(request.POST, request.FILES, instance=pattern)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated pattern!')
            return redirect('pattern-detail', pattern_id=pattern.id)
        else:
            messages.error(request, 'Failed to update pattern. Please ensure the form is valid.')
    else:
        form = PatternForm(instance=pattern)
        messages.info(request, f'You are editing {pattern.name}')

    return render(request, 'patterns/edit_pattern.html', {
        'form': form,
        'pattern': pattern,
        'MEDIA_URL': settings.MEDIA_URL
    })


@login_required
def delete_pattern(request, pattern_id):
    """Delete a pattern from the store after confirmation"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    pattern = get_object_or_404(Pattern, pk=pattern_id)

    if request.method == 'POST':  # If the form is submitted to confirm the deletion
        pattern.delete()
        messages.success(request, 'Pattern deleted!')
        return redirect(reverse('patterns'))

    # If it's a GET request, show the confirmation page
    return render(request, 'patterns/confirm_delete.html', {'pattern': pattern})

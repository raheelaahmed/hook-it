from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order, OrderLineItem
from django.contrib.auth.decorators import login_required
from django.conf import settings


@login_required
def profile(request):
    """ Display the user's profile. """
    currency_symbol = "€"
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.'
            )
    else:
        form = UserProfileForm(instance=profile)
        orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
        'MEDIA_URL': settings.MEDIA_URL,
        'currency_symbol': currency_symbol,
    }

    return render(request, template, context)


def order_history(request, order_number):
    currency_symbol = "€"
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(
        request, (
            f'This is a past confirmation for order number {order_number}. '
            'A confirmation email was sent on the order date.'
        )
    )

    order_line_items = OrderLineItem.objects.filter(order=order)

    # Generate a list of patterns
    # (and their download links) from the order line items
    patterns_with_download = []
    for item in order_line_items:
        pattern = item.pattern
        if pattern.pattern:  # Check if the pattern file exists
            patterns_with_download.append({
                'pattern_name': pattern.name,
                'pattern_url': pattern.pattern.url
            })
        else:
            patterns_with_download.append({
                'pattern_name': pattern.name,
                'pattern_url': None
            })

    template = 'checkout/checkout_success.html'

    context = {
        'order': order,
        'from_profile': True,
        'patterns_with_download': patterns_with_download,
        'currency_symbol': currency_symbol,
    }

    return render(request, template, context)

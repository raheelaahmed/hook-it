from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from patterns.models import Pattern
from django.conf import settings

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html', {'MEDIA_URL': settings.MEDIA_URL})


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    pattern = get_object_or_404(Pattern, pk=item_id)
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url', '/')
    bag = request.session.get('bag', {})

    if str(item_id) in bag:
        bag[str(item_id)] += quantity
        messages.success(
            request,
            f'Updated quantity of {pattern.name} in your bag.'
        )
    else:
        bag[str(item_id)] = quantity
        messages.success(request, f'Added {pattern.name} to your bag.')

    request.session['bag'] = bag
    print(request.session['bag'])  # Debugging
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust the quantity of an item in the shopping bag """
    pattern = get_object_or_404(Pattern, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request,
            f'Updated quantity of {pattern.name} to {quantity} in your bag.'
        )
    else:
        bag.pop(item_id, None)
        messages.info(request, f'Removed {pattern.name} from your bag.')

    request.session['bag'] = bag
    return redirect('view_bag')


def remove_from_bag(request, item_id):
    """ Function for removing items from the basket """
    try:
        bag = request.session.get('bag', {})
        if item_id in bag:
            bag.pop(item_id)
            request.session['bag'] = bag
            messages.success(request, "Item removed from your bag.")
        return redirect('view_bag')
    except Exception:
        messages.error
        (request, "Oops, something went wrong. Please try again.")
        return redirect('view_bag')

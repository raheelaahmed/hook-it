from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from patterns.models import Pattern  # Make sure to import the model

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    pattern = get_object_or_404(Pattern, pk=item_id)
    quantity = int(request.POST.get('quantity', 1))

    redirect_url = request.POST.get('redirect_url', '/')

    bag = request.session.get('bag', {})

    if str(item_id) in bag:
        bag[str(item_id)] += quantity
        messages.success(request, f'Updated quantity of {pattern.name} in your bag.')
    else:
        # Otherwise, add the new item with the specified quantity
        bag[str(item_id)] = quantity
        messages.success(request, f'Added {pattern.name} to your bag.')

    # Save the updated bag to the session
    request.session['bag'] = bag

    # Optional: Print the current session bag to the console (for debugging purposes)
    print(request.session['bag'])

    # Redirect to the provided URL
    return redirect(redirect_url)


# adjust shopping bag
def adjust_bag(request, item_id):

    """ Adjust the quantity of an item in the shopping bag """
    # Get the pattern object or return a 404 error if not found
    pattern = get_object_or_404(Pattern, pk=item_id)

    # Get the new quantity from the POST data
    quantity = int(request.POST.get('quantity'))
    
    # Get the current shopping bag from the session
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Updated quantity of {pattern.name} to {quantity} in your bag.')
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
            bag.pop(item_id)  # Remove the item from the bag
            request.session['bag'] = bag
            messages.success(request, "Item removed from your bag.")

        return redirect('view_bag')  # Redirect to the page where the bag is displayed
    except Exception as e:
        messages.error(request, "Oops, something went wrong. Please try again.")
        return redirect('view_bag')

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
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)

def adjust_bag(request, item_id):
    """ Adjust the quantity of an item in the shopping bag """
    pattern = get_object_or_404(Pattern, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id, None)  

    request.session['bag'] = bag
    return redirect('view_bag')

def remove_from_bag(request, item_id):
    """ Function for removing items from basket """
    try:
        bag = request.session.get('bag', {})
        bag.pop(item_id, None)  

        request.session['bag'] = bag
        return redirect('view_bag')
    except Exception as e:
        
        messages.error(request, "Oops, that didn't work, please try again.")
        return redirect('home')

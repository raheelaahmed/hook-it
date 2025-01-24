from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from patterns.models import Pattern

def bag_contents(request):

    bag_items = []
    total = 0
    pattern_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        pattern = get_object_or_404(Pattern, pk=item_id)
        total += quantity * pattern.price
        pattern_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'pattern': pattern,
        })
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'pattern_count': pattern_count,

    }

    return context
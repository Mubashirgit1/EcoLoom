from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from products.models import Product
# Create your views here.
def view_bag(request):
    """"View function for shopping bag."""
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """"Add a quantity of the specified product to the shopping bag."""
    # Implementation goes here
    product = Product.objects.get(pk=item_id)

    quanity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size =None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
        item_id = f"{item_id}_{size}"        
    bag = request.session.get('bag', {})
    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quanity
            else:
                bag[item_id]['items_by_size'][size] = quanity
        else:
            bag[item_id] = {'items_by_size': {size: quanity}}
    else:           
        if item_id in bag:
            bag[item_id] += quanity
        else:
            bag[item_id] = quanity
            messages.success(request, f'Added {product.name} to your bag')        
    request.session['bag'] = bag
    return redirect(redirect_url)

def adjust_bag(request, item_id):
    """"Adjust a quantity of the specified product to the specified amount."""
    # Implementation goes here
    quantity = int(request.POST.get('quantity'))
    size =None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})
    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
    else:           
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)
        
            
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

def remove_from_bag(request, item_id):
    """"Remove the specified item from the shopping bag."""
    # Implementation goes here
    try:
        size =None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})
        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            
        else:           
            bag.pop(item_id)
            
                
        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
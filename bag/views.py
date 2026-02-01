from django.shortcuts import render, redirect

# Create your views here.
def view_bag(request):
    """"View function for shopping bag."""
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """"Add a quantity of the specified product to the shopping bag."""
    # Implementation goes here
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
            
    request.session['bag'] = bag
    return redirect(redirect_url)
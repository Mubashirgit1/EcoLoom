from django.shortcuts import render

# Create your views here.
def view_bag(request):
    """"View function for shopping bag."""
    return render(request, 'bag/bag.html')
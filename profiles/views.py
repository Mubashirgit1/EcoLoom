from django.shortcuts import render

# Create your views here.
def profile(request):
    template = 'profile/profiles.html'
    context = {}
    return render(request,template,context)


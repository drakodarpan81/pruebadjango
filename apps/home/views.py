from django.shortcuts import render
#from django.contrinb.auth.decorators import login_required

# Create your views here.
#@login_required
def home(request):
    return render(request, 'home.html')
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from . models import real
# Create your views here.
@login_required(login_url='login')
def reals(request):
    rea = real.objects
    return render(request, 'Realestate/real.html', {'rea': rea})
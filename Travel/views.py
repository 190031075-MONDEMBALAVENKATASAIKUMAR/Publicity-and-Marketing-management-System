from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Tra
# Create your views here.
@login_required(login_url='login')
def trav(request):
    travelling = Tra.objects
    return render(request,'travel/travel.html',{'travelling':travelling})

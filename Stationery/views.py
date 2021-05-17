from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import station
# Create your views here.
@login_required(login_url='login')
def stationerys(request):
    stationery = station.objects
    return render(request,'Stationery/stationery.html',{'stationery':stationery})
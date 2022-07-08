from django.shortcuts import render, redirect
from . models import samsungp,realmep,applep,epsonp,contactu
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm,contactform
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'electronics/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')
        context = {}
        return render(request, 'electronics/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def elec(request):
    if request.method == "POST":
        form = contactform(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Details added successfully.")
            return redirect('yes')
        messages.add_message(request, messages.ERROR, "Details rejected. Invalid information.")
    else:
        form = contactform
    return render(request=request, template_name="electronics/home.html", context={"service1": form})


@login_required(login_url='login')
def electric(request):
    electronics = samsungp.objects
    return render(request, 'electronics/samsung.html', {'electronics': electronics})

@login_required(login_url='login')
def real(request):
    realme = realmep.objects
    return render(request, 'electronics/realme.html', {'realme': realme})

@login_required(login_url='login')
def apple(request):
    apples = applep.objects
    return render(request, 'electronics/apple.html', {'apples': apples})

@login_required(login_url='login')
def epson(request):
    epsons = epsonp.objects
    return render(request, 'electronics/epson.html', {'epsons': epsons})

@login_required(login_url='login')
def ellec(request):
    return render(request,'electronics/elect.html')

@login_required(login_url='login')
def about(request):
    return render(request,'electronics/about.html')

@login_required(login_url='login')
def pay(request,name):
    a=samsungp.objects.filter(name=name)
    return render(request,"electronics/payment.html",{'a':a})

@login_required(login_url='login')
def pay2(request,name):
    a=realmep.objects.filter(name=name)
    return render(request,"electronics/pay2.html",{'a':a})

@login_required(login_url='login')
def pay3(request,name):
    a=applep.objects.filter(name=name)
    return render(request,"electronics/pay3.html",{'a':a})

@login_required(login_url='login')
def pay4(request,name):
    a=epsonp.objects.filter(name=name)
    return render(request,"electronics/pay4.html",{'a':a})

@login_required(login_url='login')
def contacts(request):
    if request.method == "POST":
        form = contactform(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Details added successfully.")
            return redirect('yes')
        messages.add_message(request, messages.ERROR, "Details rejected. Invalid information.")
    else:
        form = contactform
    return render(request=request, template_name="electronics/contact.html", context={"service1": form})

@login_required(login_url='login')
def yes(request):
    return render(request,'electronics/yes.html')

@login_required(login_url='login')
def thank(request):
    return render(request,'electronics/Thankyou.html')

@login_required(login_url='login')
def otp(request):
    return render(request,'electronics/otp.html')

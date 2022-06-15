from django.shortcuts import render, redirect
# from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login ,logout
from django.http import HttpResponse, HttpResponseRedirect

# User = get_user_model()

# Import Product Model
from .models import Product

# Frontend
def index(request):
    # return HttpResponse('My Stock App')
    return render(request, 'frontend/index.html')


def about(request):
    return render(request, 'frontend/about.html')


def contact(request):
    return render(request, 'frontend/contact.html')


# Auth
def login_request(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            # return HttpResponseRedirect("backend/dashboard")
            return redirect("dashboard")
        else:
            return HttpResponse("Incorrect user<br><a href=""/login"">Get back login page</a>")
    return render(request, 'auth/login.html')



def logout_request(request):
    logout(request)
    return redirect("login")


def register(request):
    return render(request, 'auth/register.html')


# Backend
@login_required(login_url='/login')    
def dashboard(request):
    return render(request, 'backend/dashboard.html')


@login_required(login_url='/login')    
def products(request):
    products = Product.objects.all() # อ่านข้อมูลทั้งหมดจาก Model
    return render(request, 'backend/products.html', {'products': products})


@login_required(login_url='/login')    
def category(request):
    return render(request, 'backend/category.html')
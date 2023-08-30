from django.shortcuts import render, redirect
from .models import ArtPiece, Category
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.

def products(request):
    catid = request.GET.get('categories')
    if catid:
        prod = ArtPiece.objects.filter(category=catid)
    else:
        prod = ArtPiece.objects.all()

    context = {"products": prod,
               "categories": Category.objects.all()}
    return render(request, "products.html", context=context)


def art(request, art_id: int):
    product = ArtPiece.objects.get(pk=art_id)
    context = {"product": product}
    return render(request, "art.html", context=context)


def success(request):
    return render(request, "successMessage.html")


def payment(request, art_id: int):
    product = ArtPiece.objects.get(pk=art_id)
    context = {"product": product}
    return render(request, "payment.html", context=context)


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email,
                                                first_name=first_name, last_name=last_name)
                user.set_password(password)
                user.save()
                return redirect('login_user')
        else:
            messages.error(request, 'Passwords do not match')
            return render(request, "register.html", {'error': 'Passwords do not match'})
    else:
        return render(request, "register.html")


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('products')
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('login_user')
    else:
        return render(request, "login.html")


def logout_user(request):
    auth.logout(request)
    return redirect('products')


def search_products(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        arts = ArtPiece.objects.filter(name__contains=searched)
        return render(request, "search_products.html", {'searched': searched,
                                                        'arts': arts,
                                                        "categories": Category.objects.all()})
    else:
        return render(request, "search_products.html")

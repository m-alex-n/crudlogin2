from django.shortcuts import render, redirect
from .models import Item
from django.contrib import messages
import os
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='loginpage')
def home(request):
    products = Item.objects.all()
    context = {'products': products}
    return render(request, 'dezi/home.html', context)


def landingpage(request):
    return render(request, 'dezi/landingpage.html')


@login_required(login_url='loginpage')
def addProduct(request):
    if request.method == 'POST':
        prod = Item()
        prod.name = request.POST.get('name')
        prod.description = request.POST.get('description')
        prod.price = request.POST.get('price')

        # check if an image was uploaded
        if len(request.FILES) != 0:
            prod.image = request.FILES['image']

        prod.save()
        messages.success(request, 'Product added successfully')
        return redirect('home')

    return render(request, 'dezi/add.html')


@login_required(login_url='loginpage')
def editProduct(request, pk):
    prod = Item.objects.get(id=pk)

    if request.method == 'POST':
        # check if there is a file in the form submitted
        if len(request.FILES) != 0:
            # if there is already an existing file then delete it
            if len(prod.image) > 0:
                os.remove(prod.image.path)
                prod.image = request.FILES['image']
        prod.name = request.POST.get('name')
        prod.description = request.POST.get('description')
        prod.price = request.POST.get('price')

        # update
        prod.save()
        messages.success(request, 'Product updated successfully')
        return redirect('home')

    context = {'prod': prod}
    return render(request, 'dezi/edit.html', context)


@login_required(login_url='loginpage')
def deleteProduct(request, pk):
    prod = Item.objects.get(id=pk)
    # check if there is an image
    if len(prod.image) > 0:
        # delete file on folder
        os.remove(prod.image.path)

    # delete item in database
    prod.delete()
    messages.success(request, 'Product deleted successfully')
    return redirect('home')


def handling_404(request, exceptions):
    return render(request, 'dezi/404.html')

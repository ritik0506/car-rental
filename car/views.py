from django.http import HttpResponse
from django.shortcuts import render

from car.models import Contact

# Create your views here python functions.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def product(request):
    return render(request, 'product.html')

def login(request):
    return render(request, 'login.html')

def contact(request):
    return render(request, 'contact.html')

def create(request):
    return render(request, 'create.html')

def rent(request):
    return render(request, 'pick.html')


# for saving information into admin pannel
def Contact(request):

    if request.method=="POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()
        return HttpResponse("data is shared")

    
    

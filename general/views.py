from django.shortcuts import render, redirect, reverse
from django.core.files.storage import FileSystemStorage
from .models import User
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(req):
    return render(req, 'index.html')

def validate(req):
    email = req.POST["email"]
    password = req.POST["password"]
    try:
        v = User.objects.get(email = email,password = password)
        if v is not None:
            req.session['userid']= v.id
            return redirect(reverse('loggedin:tasks'))
    except ObjectDoesNotExist or ValueError:
        pass
    return redirect('general:index')
    
def createUser(req):
    email = req.POST["email"]
    name = req.POST["name"]
    password = req.POST["password"]
    contact = req.POST["contact"]
    File = req.FILES["image"]
    if User.objects.filter(email = email).exists():
        return render(req, 'index.html')
    image=File.name
    fs=FileSystemStorage()
    fs.save(image,File)
    c = User(name = name, contact = contact, email = email, password = password, image = image)
    c.save()
    return render(req, 'index.html')

def signup(req):
    return render(req, 'signup.html')
    
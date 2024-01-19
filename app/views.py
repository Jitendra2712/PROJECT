from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Recipe,Pic
from .forms import RecipeForm

# Create your views here.
def homeview(request):
    img = Pic.objects.all()
    return render(request,'home.html',{'img':img})

def indexview(request):
    return render(request,'index.html')

def index2view(request):
    people = [
        {'name': 'abijit', 'age': '26'},
        {'name': 'abddd', 'age': '26'},

    ]
    return render(request,'index2.html',context={'people': people})


def registerview(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        usr = User(username=username,email=email,first_name=first_name, last_name=last_name)
        usr.set_password(password)
        usr.save()

    return render(request,'register.html')

def loginview(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        usr = authenticate(username=username,password=password)
        if usr is None:
            messages.info(request,'invalid user or password')
            return redirect('login')
        
        login(request,usr)
        return redirect('home')
    return render(request,'login.html')

def logoutview(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
    
def addview(request):
    if request.method == 'POST':
        recipe_name = request.POST['recipe_name']
        recipe_price = request.POST['recipe_price']

        data = Recipe(recipe_name = recipe_name,recipe_price = recipe_price)
        data.save()
        return redirect('show')
    return render(request,'add.html')


def showview(request):
    data = Recipe.objects.all()
    con = {'data':data}
    return render(request,'show.html',con)


def editview(request,id):
    if request.method == 'POST':
        edit = Recipe.objects.get(pk=id)
        form = RecipeForm(request.POST,instance=edit)

        if form.is_valid():
            form.save()
            return redirect('show')
        

    edit = Recipe.objects.get(pk=id)
    form = RecipeForm(instance=edit)


    return render(request,'edit.html',{'form':form})

        


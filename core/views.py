from django.shortcuts import render, redirect
from competitions.models import Competition, Category
from .forms import SignupForm, LoginForm
# Create your views here.
def index(request):
    categories = Category.objects.all()
    competitions = Competition.objects.all().order_by('-created_at')
    return render(request, "core/index.html",{
        "competitions":competitions,
        "categories":categories
    })
def contact(request):
    return render(request, 'core/contact.html')
def about(request):
    return render(request, 'core/about.html')

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')


    form = SignupForm()
    return render(request, 'core/signup.html', {
        'form': form
    })

def login(request):
    form = LoginForm()
    return render(request, 'core/login.html', {
        'form': form,
    })

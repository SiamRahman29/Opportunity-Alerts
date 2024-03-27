from django.shortcuts import render
from competitions.models import Competition, Category
# Create your views here.
def index(request):
    categories = Category.objects.all()
    competitions = Competition.objects.all().order_by('-created_at')
    return render(request, "core/index.html",{
        "competitions":competitions,
        "categories":categories
    })
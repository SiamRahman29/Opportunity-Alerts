from django.shortcuts import render, get_object_or_404
from .models import Competition, Category
# Create your views here.
def detail(request, pk):
    competition = get_object_or_404(Competition, pk=pk)
    similar_competitions = Competition.objects.filter(category = competition.category, has_passed = False).exclude(pk=pk)[0:3]
    return render(request, "competitions/details.html",{
        "competition":competition,
        "similar_competitions":similar_competitions
    })
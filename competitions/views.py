from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Competition
from .forms import NewItemForm, EditItemForm
# Create your views here.
def detail(request, pk):
    competition = get_object_or_404(Competition, pk=pk)
    similar_competitions = Competition.objects.filter(category = competition.category, has_passed = False).exclude(pk=pk)[0:3]
    return render(request, "competitions/details.html",{
        "competition":competition,
        "similar_competitions":similar_competitions
    })

@login_required
def new(request):
    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('competitions:detail', pk = item.id)
    else:
        form = NewItemForm()
    return render(request, "competitions/new.html",{
        "form":form,
        "title": 'New Item'
    })

@login_required
def delete(request, pk):
    item = get_object_or_404(Competition, pk=pk, created_by = request.user)
    item.delete()

    return redirect('dashboard:index')

@login_required
def edit(request, pk):
    item = get_object_or_404(Competition, pk=pk, created_by = request.user)
    if request.method == "POST":
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('competitions:detail', pk = item.id)
    else:
        form = EditItemForm(instance=item)
    return render(request, "competitions/form.html",{
        "form":form,
        "title": 'Edit Item'
    })

from django.shortcuts import render, redirect
from .forms import IdeaForm
from .models import Idea

def create_idea(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ideas_list')
    else:
        form = IdeaForm()
    return render(request, 'ideasapp/create_idea.html', {'form': form})

def edit_idea(request, pk):
    idea = Idea.objects.get(pk=pk)
    if request.method == 'POST':
        form = IdeaForm(request.POST, instance=idea)
        if form.is_valid():
            form.save()
            return redirect('ideas_list')
    else:
        form = IdeaForm(instance=idea)
    return render(request, 'ideasapp/edit_idea.html', {'form': form})

def delete_idea(request, pk):
    idea = Idea.objects.get(pk=pk)
    if request.method == 'POST':
        idea.delete()
        return redirect('ideas_list')
    return render(request, 'ideasapp/delete_idea.html', {'idea': idea})

def ideas_list(request):
    ideas = Idea.objects.all()
    return render(request, 'ideasapp/ideas_list.html', {'ideas': ideas})

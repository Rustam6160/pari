from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import GoodDeed
from .forms import GoodDeedForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def home(request):
    query = request.GET.get('q')
    if query:
        deeds = GoodDeed.objects.filter(title__icontains=query)
    else:
        deeds = GoodDeed.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'deeds': deeds, 'query': query})

@login_required
def add_deed(request):
    if request.method == 'POST':
        form = GoodDeedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = GoodDeedForm()
    return render(request, 'add_deed.html', {'form': form})

@login_required
def edit_deed(request, pk):
    deed = get_object_or_404(GoodDeed, pk=pk)
    form = GoodDeedForm(request.POST or None, instance=deed)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'edit_deed.html', {'form': form})

@login_required
def delete_deed(request, pk):
    deed = get_object_or_404(GoodDeed, pk=pk)
    if request.method == 'POST':
        deed.delete()
        return redirect('home')
    return render(request, 'delete_deed.html', {'deed': deed})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

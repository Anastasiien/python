from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import CollectionItem
from .forms import CollectionItemForm, RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('collection_list')
    else:
        form = RegisterForm()
    return render(request, 'auth/register.html', {'form': form})

@login_required
def collection_list(request):
    items = CollectionItem.objects.filter(owner=request.user)
    return render(request, 'app/collection_list.html', {'items': items})

@login_required
def collection_create(request):
    if request.method == 'POST':
        form = CollectionItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            item.save()
            form.save_m2m()  # для ManyToMany
            return redirect('collection_list')
    else:
        form = CollectionItemForm()
    return render(request, 'app/collection_form.html', {'form': form})

@login_required
def collection_update(request, pk):
    item = get_object_or_404(CollectionItem, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = CollectionItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('collection_list')
    else:
        form = CollectionItemForm(instance=item)
    return render(request, 'app/collection_form.html', {'form': form})

@login_required
def collection_delete(request, pk):
    item = get_object_or_404(CollectionItem, pk=pk, owner=request.user)
    if request.method == 'POST':
        item.delete()
        return redirect('collection_list')
    return render(request, 'app/collection_confirm_delete.html', {'item': item})
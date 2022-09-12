from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import StoreForm
from .models import Store


def add_item(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item Added Successfully')

            return redirect('/')
    else:
        form = StoreForm()
    return render(request, 'index.html', {'form': form})


def summary(request):
    items = Store.objects.all()
    total_price = 0
    for item in items:
        total_price += item.price
    return render(request, 'summary.html', {'total_price': total_price})

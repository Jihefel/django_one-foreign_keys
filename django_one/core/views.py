from django.shortcuts import render, redirect
from .models import Pays, President
from .forms import PaysForm, PresidentForm

def index(request):
    return render(request, 'core/index.html')

def pays_crud(request):
    if request.method == 'POST':
        form = PaysForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pays_crud')
    else:
        form = PaysForm()
    
    pays = Pays.objects.all()
    context = {'form': form, 'pays': pays}
    return render(request, 'core/pays_crud.html', context)


def president_crud(request):
    if request.method == 'POST':
        form = PresidentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('president_crud')
    else:
        form = PresidentForm()

    presidents = President.objects.all()
    context = {'form': form, 'presidents': presidents}
    return render(request, 'core/president_crud.html', context)

from django.shortcuts import render, redirect
from .models import Drug, Factory
from .forms import DrugForm
from django.db.models import Count, Max, Min, Avg, Sum

# Create your views here.
def drug_list(request):
    if request.method == 'POST':
        form = DrugForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = DrugForm()
    drugs_query_set = Drug.objects.all()
    info = Drug.objects.aggregate(
        say=Count('title'),
        ortalama=Avg('price'),
        maks=Max('price'),
        minimum=Min('price'),
        toplam=Sum('price'),
    )
    return render(request, 'drug-list.html', context={
        'drugs': drugs_query_set,
        'factories': Factory.objects.all(),
        'form': form,
        'info': info,
    })

def delete_drug(request, pk):
    drug = Drug.objects.filter(pk=pk).first()
    if drug:
        drug.delete()
        return redirect('drug-list')
    else:
        return redirect('drug-list')


def update_drug(request, pk):
    if request.method == 'GET':
        form = DrugForm(instance=Drug.objects.get(pk=pk))
    elif request.method =='POST':
        form = DrugForm(request.POST, instance=Drug.objects.get(pk=pk))
        if form.is_valid():
            form.save()
            return redirect('drug-list')
    return render(request, 'drug-edit.html', context={'form': form, 'id': pk})


def factory_list(request):
    factories = Factory.objects.all().annotate(
        say=Count('drug'),
        ortalama=Avg('drug__price'),
        cem=Sum('drug__price')
    )

    return render(request, 'factory-list.html', context={
        'factories': factories,
    })
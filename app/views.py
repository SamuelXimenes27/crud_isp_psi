from datetime import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from app.forms import AnimalsForm, ServiceOrdersForm
from app.models import Animals, ServiceOrders
from django.core.paginator import Paginator


def home(request):
    # Filtro procurar
    dataClient = {}
    searchClient = request.GET.get('search')
    if searchClient:
        dataClient['database'] = Animals.objects.filter(
            cpf__icontains=searchClient)

    else:
        dataClient['database'] = Animals.objects.all()

    dataOS = {}
    searchOS = request.GET.get('search')
    if searchOS:
        dataOS['databaseOS'] = ServiceOrders.objects.filter(
            technician_name__icontains=searchOS)

    else:
        dataOS['databaseOS'] = ServiceOrders.objects.all()

    return render(request, 'main/home.html', dataOS | dataClient)


def dashboard(request):
    data = {}
    data['database'] = AnimalsForm()
    return render(request, 'main/dashboard.html', data)

###########################################################################################
# Client Form - Start


def form(request):
    data = {}
    data['form'] = AnimalsForm()
    return render(request, 'main/form.html', data)


def create(request):
    form = AnimalsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


def edit(request, pk):
    data = {}
    data['database'] = Animals.objects.get(pk=pk)
    data['form'] = AnimalsForm(instance=data['database'])
    return render(request, 'main/form.html', data)


def update(request, pk):
    data = {}
    data['database'] = Animals.objects.get(pk=pk)
    form = AnimalsForm(request.POST or None, instance=data['database'])
    if form.is_valid():
        form.save()
        return redirect('home')


def delete(request, pk):
    database = Animals.objects.get(pk=pk)
    database.delete()
    return redirect('home')
# Client Form - End
###########################################################################################

###########################################################################################
# Service Order Form - Start


def formOS(request):
    data = {}
    data['formOS'] = ServiceOrdersForm()
    return render(request, 'main/formOS.html', data)


def createOS(request):
    formOS = ServiceOrdersForm(request.POST or None)
    if formOS.is_valid():
        formOS.save()
        return redirect('home')


def editOS(request, pk):
    data = {}
    data['database'] = ServiceOrders.objects.get(pk=pk)
    data['formOS'] = ServiceOrdersForm(instance=data['database'])
    return render(request, 'main/formOS.html', data)


def updateOS(request, pk):
    data = {}
    data['database'] = ServiceOrders.objects.get(pk=pk)
    formOS = ServiceOrdersForm(request.POST or None, instance=data['database'])
    if formOS.is_valid():
        formOS.save()
        return redirect('home')


def deleteOS(request, pk):
    database = ServiceOrders.objects.get(pk=pk)
    database.delete()
    return redirect('home')
# Service Order Form - End
###########################################################################################

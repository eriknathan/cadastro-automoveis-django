from django.shortcuts import render, redirect
from app.forms import VinhosForm
from app.scripts.user_model import using_model


# Create your views here.
def home(request):
    data = using_model()
    return render(request, 'index.html', {'predicao': data})


def form(request):
    data = {}
    data['form'] = VinhosForm()
    return render(request, 'form.html', data)


def create(request):
    form = VinhosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


# def view(request, pk):
#     data = {}
#     data['db'] = Vinhos.objects.get(pk=pk)
#     return render(request, 'view.html', data)


# def edit(request, pk):
#     data = {}
#     data['db'] = Vinhos.objects.get(pk=pk)
#     data['form'] = VinhosForm(instance=data['db'])
#     return render(request, 'form.html', data)


# def update(request, pk):
#     data = {}
#     data['db'] = Vinhos.objects.get(pk=pk)
#     form = VinhosForm(request.POST or None, instance=data['db'])
#     if form.is_valid():
#         form.save()
#         return redirect('home')


# def delete(request, pk):
#     db = Vinhos.objects.get(pk=pk)
#     db.delete()
#     return redirect('home')

from django.shortcuts import redirect, render

from app.forms import VinhosForm
from app.scripts.user_model import using_model
from app.scripts.view_dbs import database


# Create your views here.
def home(request):
    data = using_model()
    dbs = database()
    return render(request, 'index.html', {'predicao': data, 'db': dbs})


def form(request):
    data = {}
    data['form'] = VinhosForm()
    return render(request, 'form.html', data)


def create(request):
    form = VinhosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

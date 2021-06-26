from django.forms.widgets import MultipleHiddenInput
from django.shortcuts import render,redirect
from .models import periodista
from .forms import formu_p
# Create your views here.
def index(request):

    return render(request,'index.html')


def form_creacion(request):

    if request.method == "POST":
        formulario=formu_p(request.POST)
        if formulario.is_valid():
           formulario.save()
           return redirect('mostrar')
    else:
        formulario=formu_p()
    
    return render(request, 'core(2)/crear_p.html', {'formulario_c': formu_p})


def mostrar(request):
    personas = periodista.objects.all()
    return render (request , 'core(2)/mostrar.html', {'todos':personas})


def modificar(request,id):
    peri = periodista.objects.get(rut=id)

    datos ={
        'form':formu_p(instance=peri)
    }

    if request.method == "POST":
        personas = formu_p(data=request.post,instance=peri)
        if personas.is_valid():
            personas.save()
            return redirect('mostra')
    else:
        personas = formu_p()
    
    return render(request, 'core(2)/modificar.html', datos)

def eliminar(request,id):
    peri= periodista.objects.get(rut=id)
    peri.delete()
    
    return redirect('mostrar')
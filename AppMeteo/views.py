from django.shortcuts import render
from django.http import HttpResponse
from AppMeteo.forms import *
from AppMeteo.models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.

def InicioSesion(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contra)

            if user:
                login(request,user)

                return render(request, "AppMeteo/inicio.html", {"mensaje":f"Bienvenido {user}"})

        else:
            return render(request, "AppMeteo/inicio.html", {"mensaje": "Datos incorrectos"})

    else:
        form=AuthenticationForm()

    return render(request, "AppMeteo/login.html", {"formulario":form})

def register(request):
    if request.method == "POST":
        form=UsuarioRegistro(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "AppMeteo/inicio.html", {"mensaje":"Usuario Correcto"})

    else:
        form=UsuarioRegistro()

    return render(request, "AppMeteo/registro.html", {"formulario":form})

@login_required
def editarUsuario(request):
    usuario = request.user
    if request.method == "POST":
        form= FormularioEditar(request.POST)

        if form.is_valid():
            info=form.cleaned_data

            usuario.email = info["Email"]
            usuario.set.password(info["password1"])
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]
            usuario.save()

            return render(request, "AppMeteo/inicio.html")

    else:
        form=FormularioEditar(initial={"email":usuario.email,"first_name":usuario.first_name,"last_name":usuario.last_name}) 

    return render(request, "AppMeteo/editarPerfil.html", {"formulario":form, "usuario":usuario})



def inicio(request):
    return render(request, "AppMeteo/inicio.html")

def fenomeno(request):

    fen1 = Fenomeno(nombre="lluvia", fecha="2022-09-10")
    fen1.save()

    return render(request, "AppMeteo/fenomeno.html")


def acercademi(request):
    midato = Acercademi(info="Mi nombre es Sol y tengo 25 años. Soy técnica en meteorología y trabajo en el Servicio Meteorológico Nacional de Argentina")
    midato.save()
    return render(request, "AppMeteo/acercademi.html")


def miembro(request):
    per1 = Miembros(nombre="Tiziana", apellido="Kseminski", email="tizi@titu.com", edad="22")
    per1.save()

    return render(request, "AppMeteo/miembro.html")



def fenomenoFormulario(request):

    if request.method == "POST":

        formulario1= FenomenoFormulario(request.POST)

        if formulario1.is_valid():
            info= formulario1.cleaned_data

            fenomeno= Fenomeno(nombre=info["fenomeno"], fecha=info["fecha"])

            fenomeno.save()

            return render(request, "AppMeteo/inicio.html")

    else :
        formulario1 = FenomenoFormulario() 

    return render(request, "AppMeteo/fenomenoFormulario.html", {"form1":formulario1})



def busquedafenomeno(request):
    return render(request, "AppMeteo/fenomeno.html")


def resultados(request):

    if request.GET["fenomeno"]:
        nombre=request.GET["fenomeno"]
        fenomenos=Fenomeno.objects.filter(nombre__icontains=fenomeno)

        return render(request, "AppMeteo/fenomeno.html", {"fenomenos":fenomenos, "nombre":nombre})

    else:
        respuesta = "No enviaste datos."

    return HttpResponse(respuesta)

def busquedamiembro(request):
    return render(request, "AppMeteo/miembro.html")


def resultados(request):

    if request.GET["miembro"]:
        nombre=request.GET["miembro"]
        miembros=Miembros.objects.filter(nombre__icontains=miembro)

        return render(request, "AppMeteo/miembro.html", {"miembros": miembro, "nombre":nombre})

    else:
        respuesta = "No enviaste datos."

    return HttpResponse(respuesta)









@login_required
def leerMiembros(request):
    miembros = Miembros.objects.all()

    contexto = {"people": miembros}
    return render(request, "AppMeteo/leerMiembro.html", contexto)


def crearMiembros(request):
     if request.method == "GET":

        formulario1= MiembroFormulario(request.GET)

        if formulario1.is_valid():
            info= formulario1.cleaned_data

            miembro= Miembros(nombre=info["nombre"], apellido=info["apellido"], email=info["email"], edad=info["edad"])

            miembro.save()

            return render(request, "AppMeteo/miembroFormulario.html")

        else :
            formulario1 = MiembroFormulario() 

        return render(request, "AppMeteo/inicio.html", {"formulario1":formulario1})




def eliminarMiembros(request, miembroNombre):
    miembro = Miembros.objects.get(nombre=miembroNombre)
    miembro.delete()

    miembros = Miembros.objects.all()
    contexto = {"people": miembros}

    return render(request, "AppMeteo/leerMiembro.html", contexto)


def editarMiembro(request, miembroNombre):
    miembro = Miembros.objects.get(nombre=miembroNombre)

    if request.method == "GET" :
        formulario1= MiembroFormulario(request.GET)

        if formulario1.is_valid():
            info= formulario1.cleaned_data

            miembro.nombre = info["nombre"]
            miembro.apellido = info["apellido"]
            miembro.email = info["email"]
            miembro.edad = info["edad"]

            miembro.save()

            return render(request, "AppMeteo/inicio.html")

        else :
            formulario1 = MiembroFormulario(initial={"nombre":miembro.nombre, "apellido":miembro.apellido, "email":miembro.email, "edad":miembro.edad}) 

        return render(request, "AppMeteo/editarMiembro.html", {"formulario1":formulario1, "nombre":miembroNombre})

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)

        if form.is_valid():
            usuarioActual = User.objects.get(username=request.user)
            avatar = Avatar(usuario=usuarioActual, imagen=form.cleaned_data["imagen"])
            avatar.save()

            return render(request, "AppMeteo/inicio.html")

    else:
        form = AvatarFormulario()

    return render(request, "AppMeteo/agregarAvatar.html", {"formulario": form})










class ListaFenomeno(LoginRequiredMixin, ListView):
    model = Fenomeno

class DetalleFenomeno(LoginRequiredMixin,DetailView):
    model = Fenomeno

class CrearFenomeno(LoginRequiredMixin,CreateView):
    model = Fenomeno 
    succes_url = "/AppMeteo/fenomeno/list"
    fields = ["nombre", "fecha"]

class ActualizarFenomeno(LoginRequiredMixin,UpdateView):
    model = Fenomeno 
    succes_url = "/AppMeteo/fenomeno/list"
    fields = ["nombre", "fecha"]

class BorrarFenomeno(LoginRequiredMixin,DeleteView):
    model = Fenomeno
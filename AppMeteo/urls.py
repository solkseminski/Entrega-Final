from django.urls import path
from AppMeteo.views import *
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path("", inicio, name="Inicio"),
    path('fenomenos/', fenomeno, name="Fenomeno"),
    path('about/', acercademi, name="Acercademi"),
    path('miembros/', miembro, name="Miembros"),
    path('fenomenoFormulario/', fenomenoFormulario, name="FormularioFenomeno"),  
    path('buscarfenomeno/', busquedafenomeno, name="BuscarFenomeno"),
    path('resultados/', resultados, name="ResultadosFenomeno"),
    path('buscarmiembro/', busquedamiembro, name="BuscarMiembro"),
    path('resultadosmiembro/', resultados, name="ResultadosMiembro"),
    path('login/', InicioSesion, name="Login"),
    path('register/', register, name="Signup"),
    path('logout', LogoutView.as_view(template_name="AppMeteo/logout.html"), name="Logout"),
    path('editar/', editarUsuario, name="UsuarioEditar"),
    path('agregar/', agregarAvatar, name="AvatarAgregar"),





    #CRUD DE MIEMBROS
    path('leerMiembro/', leerMiembros, name="MiembrosLeer"), 
    path('crearMiembro/', crearMiembros, name="MiembrosCrear"), 
    path('eliminarMiembro/<miembroNombre>/', eliminarMiembros, name="MiembroEliminar"),
    path('editarMiembro/<miembroNombre>/', editarMiembro, name="MiembroEditar"),


    #CRUD DE FENOMENOS USANDO CLASES
    path('fenomeno/list/', ListaFenomeno.as_view(), name="FenomenosLeer"),
    path('fenomeno/<int:pk>/', DetalleFenomeno.as_view(), name="FenomenosDetalle"),
    path('fenomeno/crear/', CrearFenomeno.as_view(), name="FenomenosCrear"),
    path('fenomeno/editar/<int:pk>', ActualizarFenomeno.as_view(), name="FenomenosEditar"),
    path('fenomeno/borrar/<int:pk>', BorrarFenomeno.as_view(), name="FenomenosBorrar"),

]   

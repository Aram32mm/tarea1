from ast import Num
from nntplib import GroupInfo
from termios import FF1
from django.shortcuts import render
from rest_framework import generics, viewsets
from . serializers import RetoSerializer, JugadorSerializer, UsuarioSerializer, PartidaSerializer
from . models import Reto, Jugadores, Usuario, Partida
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads, dumps 
from fractions import Fraction
from .models import Reto
import sqlite3
import requests

# Create your views here 
def nueva():
    return 0

def index(request):
    #return HttpResponse("Bienvenido")
    return render(request,'index.html')

def procesamiento(request):
    nombre = request.POST['nombre']
    nombre = nombre.title()
    return render(request, 'proceso.html',{'name':nombre})
    
def lista(request):
    jugadores = Reto.objects.all() #select * from Reto
    return render(request,'datos.html',{'lista_jugadores':jugadores})

@csrf_exempt
def suma(request):
    body_unicode = request.body.decode( 'utf-8')
    body = loads(body_unicode)
    frac1 = Fraction(body['numerador1'],body['denominador1'])
    frac2 = Fraction(body['numerador2'],body['denominador2'])
    resultado = frac1 + frac2
    #json_resultado = resultado.toJSON()
    json_resultado = dumps({"num":int(resultado.numerator), "den":int(resultado.denominator)}, sort_keys=False, indent=4)
    return HttpResponse(json_resultado,content_type = "text/json-comment-filtered")

@csrf_exempt
def resta(request):
    body_unicode = request.body.decode( 'utf-8')
    body = loads(body_unicode)
    frac1 = Fraction(body['numerador1'],body['denominador1'])
    frac2 = Fraction(body['numerador2'],body['denominador2'])
    resultado = frac1 - frac2
    #json_resultado = resultado.toJSON()
    json_resultado = dumps({"num":int(resultado.numerator), "den":int(resultado.denominator)}, sort_keys=False, indent=4)
    return HttpResponse(json_resultado,content_type = "text/json-comment-filtered")


@csrf_exempt
def multiplicacion (request):
    body_unicode = request.body.decode( 'utf-8')
    body = loads(body_unicode)
    frac1 = Fraction(body['numerador1'],body['denominador1'])
    frac2 = Fraction(body['numerador2'],body['denominador2'])
    resultado = frac1 * frac2
    #json_resultado = resultado.toJSON()
    json_resultado = dumps({"num":int(resultado.numerator), "den":int(resultado.denominator)}, sort_keys=False, indent=4)
    return HttpResponse(json_resultado,content_type = "text/json-comment-filtered")


@csrf_exempt
def division(request):
    body_unicode = request.body.decode( 'utf-8')
    body = loads(body_unicode)
    frac1 = Fraction(body['numerador1'],body['denominador1'])
    frac2 = Fraction(body['numerador2'],body['denominador2'])
    resultado = frac1 / frac2
    #json_resultado = resultado.toJSON()
    json_resultado = dumps({"num":int(resultado.numerator), "den":int(resultado.denominator)}, sort_keys=False, indent=4)
    return HttpResponse(json_resultado,content_type = "text/json-comment-filtered")

def usuarios(request):
    if request.method == 'GET':
        con = sqlite3.connect("db.sqlite3")
        cur = con.cursor()
        res = cur.execute("SELECT * FROM usuarios")
        resultado = res.fetchall()
        '''
        for registro in resultado:
            id, grupo, grado, num_lista = registro
        '''
        #return HttpResponse(resultado)
        return render(request,'datosDB.html',{'lista_usuarios':resultado})
    elif request.method == 'POST':
        body = request.body.decode('UTF-8')
        eljson = loads(body)
        grupo = eljson['grupo']
        grado = eljson['grado']
        num_lista = eljson['num_lista']
        con = sqlite3.connect("db.sqlite3")
        cur = con.cursor()
        res = cur.execute("INSERT INTO usuarios (grupo, grado, num_lista) VALUES(?,?,?)",(grupo, grado, num_lista))
        con.commit()
        return HttpResponse('OK. Usuario agregado!')
    elif request.method == 'DELETE':
        return(usuario_del(request))


@csrf_exempt
def usuario_pos(request):
    body = request.body.decode('UTF-8')
    eljson = loads(body)
    grupo = eljson['grupo']
    grado = eljson['grado']
    num_lista = eljson['num_lista']
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    res = cur.execute("INSERT INTO usuarios (grupo, grado, num_lista) VALUES(?,?,?)",(grupo, grado, num_lista))
    con.commit()
    return HttpResponse('OK. Usuario agregado!')

@csrf_exempt
def usuario_del(request):
    body = request.body.decode('UTF-8')
    eljson = loads(body)
    id = eljson['id']
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    #res = cur.execute(f'DELETE FROM usuarios WHERE id_usuario = ?',(str(id)))
    res = cur.execute(f'DELETE FROM usuarios WHERE id_usuario = {id}')
    con.commit()
    return HttpResponse('OK. Usuario borrado.')

@csrf_exempt
def usuario_updt(request):
    body = request.body.decode('UTF-8')
    eljson = loads(body)
    id = eljson['id']
    grupo = eljson['grupo']
    grado = eljson['grado']
    num_lista = eljson['num_lista']
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    res = cur.execute(f'UPDATE usuarios SET grupo = ?, grado = ?, num_lista = ? WHERE id_usuario = ?',(grupo, grado, num_lista, id))
    con.commit()
    return HttpResponse('OK. Cambio de usuario exitoso.')

#servicio endpoint de validación de usuarios
#entrada: { "id_usuario" :"usuario","pass" : "contrasenia"}
#salida: {"estatus":True}
@csrf_exempt
def valida_usuario(request):
    body = request.body.decode('UTF-8')
    eljson = loads(body)
    usuario  = eljson['id_usuario']
    contrasenia = eljson['pass']
    print(usuario+contrasenia)
    #con = sqlite3.connect("db.sqlite3")
    #cur = con.cursor()
    #res = cur.execute("SELECT * FROM usuarios WHERE id_usuario=? AND password=?",(str(usuario),str(contrasenia)))
    #si el usuario es correcto regresar respuesta exitosa 200 OK
    #en caso contrario, regresar estatus false
    return HttpResponse('{"estatus":true}')

#Ruta para carga de la página web con el formulario de login
@csrf_exempt
def login(request):
    return render(request, 'login.html')

#Ruta para el proceso del login (invocación del servicio de verificación de usuario)
@csrf_exempt
def procesologin(request):
    usuario = request.POST['usuario']
    contrasenia = request.POST['password']
    #invoca el servicio de validación de usuario
    url = "http://127.0.0.1:8000/valida_usuario"
    header = {
    "Content-Type":"application/json"
    }
    payload = {   
    "id_usuario" :usuario,
    "pass" : contrasenia
    }
    result = requests.post(url,  data= dumps(payload), headers=header)
    if result.status_code == 200:
        return HttpResponse('Abrir página principal')
    return HttpResponse('Abrir página de credenciales inválidas')

class RetoViewSet(viewsets.ModelViewSet):
    queryset = Reto.objects.all()
    serializer_class = RetoSerializer
    #ModelViewSet permite crear los manejadores para GET, POST, PUT, DELETE de manera automática

class JugadoresViewSet(viewsets.ModelViewSet):
    queryset = Jugadores.objects.all() # select * from Calculadora.jugadores
    serializer_class = JugadorSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PartidaViewSet(viewsets.ModelViewSet):
    queryset = Partida.objects.all()
    serializer_class = PartidaSerializer

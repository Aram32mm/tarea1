from ast import Num
from termios import FF1
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads, dumps 
from fractions import Fraction
from .models import Reto

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
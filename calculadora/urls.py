from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'reto', views.RetoViewSet)
router.register(r'jugador', views.JugadoresViewSet)
router.register(r'usuarios', views.UsuarioViewSet, basename='usuario')
router.register(r'partidas', views.PartidaViewSet, basename='partida')
#Reto
router.register(r'estudiantes', views.EstudianteViewSet)
router.register(r'juegos', views.JuegoViewSet)
router.register(r'intentos', views.IntentosViewSet)

urlpatterns = [
    path('api/',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('',views.index, name='index'),
    path('procesamiento',views.procesamiento, name='procesamiento'),
    path('lista',views.lista,name='lista'),
    path('suma',views.suma,name='suma'),
    path('resta',views.resta,name='resta'),
    path('multiplicacion',views.multiplicacion,name='multiplicacion'),
    path('division',views.division,name='division'),
    path('usuario_lista',views.usuarios,name='usuarios'),
    path('usuario_pos',views.usuario_pos,name='usuario_pos'),
    path('usuario_del',views.usuario_del,name='usuario_del'),
    path('usuario_updt',views.usuario_updt,name='usuario_updt'),
    path('login', views.login, name='login'),
    path('procesologin', views.procesologin, name='procesologin'),
    path('valida_usuario',views.valida_usuario,name='valida_usuario'),
    path('grafica',views.grafica,name='grafica'),
    path('barras',views.barras,name='barras'),
    path('gauge',views.gauge_chart,name='gauge'),
]
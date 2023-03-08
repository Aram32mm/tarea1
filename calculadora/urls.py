from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('procesamiento',views.procesamiento, name='procesamiento'),
    path('lista',views.lista,name='lista'),
    path('suma',views.suma,name='suma'),
    path('resta',views.resta,name='resta'),
    path('multiplicacion',views.multiplicacion,name='multiplicacion'),
    path('division',views.division,name='division'),
    path('usuarios',views.usuarios,name='usuarios'),
    path('usuario_pos',views.usuario_pos,name='usuario_pos'),
    path('usuario_del',views.usuario_del,name='usuario_del'),
    path('usuario_updt',views.usuario_updt,name='usuario_updt'),
]
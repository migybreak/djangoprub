from django.urls import path
from . import views
from .views import reporte

urlpatterns = [
    path('', views.inicio),
    path('registrarCurso/', views.registrarCurso),
    path('edicionCurso/<codigo>', views.edicionCurso, name='edicionCurso'),
    path('editarCurso/', views.editarCurso),
    path('inicio/eliminarCurso/<codigo>', views.eliminarCurso, name='eliminarCurso'),
    path('talleres/', views.talleres, name='talleres'),
    path('nuevo/', views.nuevo, name='nuevo'),
    path('inicio/', views.inicio, name='inicio'),
    path('reporte/<codigo>/', views.reporte, name='reporte')
]
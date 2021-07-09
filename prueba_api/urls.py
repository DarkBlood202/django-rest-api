from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# from rest_framework import renderers
# from rest_framework.urlpatterns import format_suffix_patterns

# from .views import api_root, ReportesViewSet, PreguntaViewSet, UsuarioViewSet

router = DefaultRouter()
router.register('reportes', views.ReportesViewSet)
router.register('preguntas', views.PreguntaViewSet)
router.register('usuarios', views.UsuarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# lista_reportes = ReportesViewSet.as_view({
#     'get': 'list'
#     'post': 'create'
# })
# reporte_detalle = ReportesViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update'
#     'delete': 'destroy'
# })

# lista_preguntas = PreguntasViewSet.as_view({
#     'get': 'list'
#     'post': 'create'
# })
# pregunta_detalle = PreguntasViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update'
#     'delete': 'destroy'
# })

# lista_usuarios = UsuarioViewSet.as_view({
#     'get': 'list'
# })
# usuario_detalle = UsuarioViewSet.as_view({
#     'get': 'retrieve'
# })

# urlpatterns = [
#     path('', views.api_root),

#     path('reportes/', views.ReportesList.as_view()),
#     path('reportes/<int:pk>/', views.ReporteDetail.as_view()),
    
#     path('usuarios/', views.UsuariosList.as_view()),
#     path('usuarios/<int:pk>/', views.UsuarioDetail.as_view()),

#     path('preguntas/', views.PreguntasList.as_view()),
#     path('preguntas/<int:pk>/', views.PreguntaDetail.as_view()),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)
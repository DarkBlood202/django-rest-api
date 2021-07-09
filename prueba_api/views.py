from rest_framework import generics, permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User

from .models import Reporte, Pregunta
from .serializers import ReporteSerializer, PreguntaSerializer, UsuarioSerializer
from .permissions import IsAuthorOrReadOnly

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'usuarios': reverse('lista-usuarios', request=request, format=format),
        'reportes': reverse('lista-reportes', request=request, format=format),
        'preguntas': reverse('lista-preguntas', request=request, format=format)
    })

#################### REPORTES ####################

class ReportesViewSet(viewsets.ModelViewSet):
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer
    permission_classes = [permissions.IsAuthenticated]

# class ReportesList(generics.ListCreateAPIView):
#     queryset = Reporte.objects.all()
#     serializer_class = ReporteSerializer

#     permission_classes = [permissions.IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(usuario=self.request.user)


# class ReporteDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Reporte.objects.all()
#     serializer_class = ReporteSerializer

#     permission_classes = [permissions.IsAuthenticated]

################### PREGUNTAS ###################

class PreguntaViewSet(viewsets.ModelViewSet):
    """
    El ViewSet provee vista de lista y detalle, operaciones CUD.
    """
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsAuthorOrReadOnly
    ]

    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)

# class PreguntasList(generics.ListCreateAPIView):
#     queryset = Pregunta.objects.all()
#     serializer_class = PreguntaSerializer

#     permission_classes = [permissions.IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(autor=self.request.user)


# class PreguntaDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Pregunta.objects.all()
#     serializer_class = PreguntaSerializer

#     permission_classes = [
#         permissions.IsAuthenticated,
#         IsAuthorOrReadOnly
#     ]

################# USUARIOS #################

class UsuarioViewSet(viewsets.ReadOnlyModelViewSet):
    """
    El ViewSet provee vista de lista y de detalle.
    """
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

# class UsuariosList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UsuarioSerializer

#     permission_classes = [permissions.IsAuthenticated]


# class UsuarioDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UsuarioSerializer

#     permission_classes = [permissions.IsAuthenticated]

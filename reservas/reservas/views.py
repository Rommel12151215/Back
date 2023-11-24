from rest_framework import generics
from rest_framework import viewsets
from .models import Reserva
from .serializers import ReservaSerializer

class ReservaViewSet(viewsets.ModelViewSet):
      queryset = Reserva.objects.all()
      serializer_class = ReservaSerializer

class ReservaDestroyAPIView(generics.DestroyAPIView):
  queryset = Reserva.objects.all()
  serializer_class = ReservaSerializer
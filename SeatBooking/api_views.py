from .models import Service
from .serializers import ServiceSerializer
from rest_framework.generics import ListAPIView

class ServiceList(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

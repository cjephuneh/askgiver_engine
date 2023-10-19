# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets

from .models import CsrInitiative
from .serializers import CsrInitiativeSerializer
# Create your views here.
class CsrInitiativeView(viewsets.ModelViewSet):
    serializer_class = CsrInitiativeSerializer
    queryset = CsrInitiative.objects.all()
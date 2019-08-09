from django.shortcuts import render
from rest_framework import viewsets
from .models import EmpInfo
from .serializers import EmpInfoSerializer

# Create your views here.


class EmpInfoView(viewsets.ModelViewSet):
    queryset = EmpInfo.objects.all()
    serializer_class = EmpInfoSerializer
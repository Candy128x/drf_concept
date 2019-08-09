from rest_framework import serializers
from .models import EmpInfo


class EmpInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpInfo
        fields = ('__all__')
from rest_framework import serializers
from .models import Language, Paradigm, Programmer


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'url', 'name', 'paradigm')


class ParadigmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paradigm
        fields = ('id', 'url', 'name')


class ProgrammerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Programmer
        fields = ('id', 'url', 'name', 'languages')


class ProgLangSerializer(serializers.ModelSerializer):
    prog = ProgrammerSerializer(read_only=True)

    class Meta:
        model = Programmer
        fields = ('__all__')
        depth = 3
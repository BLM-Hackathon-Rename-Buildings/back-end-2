from symbols.models import * 
from rest_framework import serializers


class SymbolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symbol
        exclude = ['approved']


class HonoreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Honoree
        fields =  '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields =  '__all__'
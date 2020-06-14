from symbols.models import * 
from rest_framework import serializers


class SymbolLimitedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symbol
        fields = ['id', 'name', 'latitude', 'longitude', 'removed']

class SymbolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symbol
        exclude = ['approved']
        depth = 1

class HonoreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Honoree
        fields =  '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields =  '__all__'
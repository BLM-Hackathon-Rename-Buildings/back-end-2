# Create your views here.
from symbols.models import * 
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework import viewsets, response, generics
from symbols.serializers import *


# documentation note
class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class SymbolViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Symbol.objects.all().filter(approved=True).filter(symbol_type="monument") #.filter(pk__lt=961)
    serializer_class = SymbolSerializer

    def get_object(self):
        instance = super().get_object()

        data = Symbol.objects.get(pk=instance.id).to_dict()
        return response.Response(data)

class SymbolDetailCustomView(generics.RetrieveAPIView):
    queryset = Symbol.objects.all().filter(approved=True).filter(symbol_type="monument") #.filter(pk__lt=961)
    serializer_class = SymbolSerializer


    def get_object(self):
        instance = super().get_object()

        data = Symbol.objects.get(pk=instance.id).to_dict()
        return response.Response(data)

class HonoreeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Honoree.objects.all()
    serializer_class = HonoreeSerializer


class ContactViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
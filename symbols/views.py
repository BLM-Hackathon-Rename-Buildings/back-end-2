# Create your views here.
from symbols.models import * 
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework import viewsets
from symbols.serializers import *


# documentation note
class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class SymbolViewSet(viewsets.ModelViewSet):
    permission_classes=[ReadOnly]
    queryset = Symbol.objects.all().filter(approved=True).filter(symbol_type="monument") #.filter(pk__lt=961)
    serializer_class = SymbolSerializer


class HonoreeViewSet(viewsets.ModelViewSet):
    permission_classes=[ReadOnly]
    queryset = Honoree.objects.all()
    serializer_class = HonoreeSerializer


class ContactViewSet(viewsets.ModelViewSet):
    permission_classes=[ReadOnly]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
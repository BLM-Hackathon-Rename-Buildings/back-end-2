# Create your views here.
from symbols.models import * 
from rest_framework import viewsets, generics
from symbols.serializers import *



class SymbolViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Symbol.objects.all().filter(approved=True).filter(symbol_type="monument") #.filter(pk__lt=961)
    serializer_class = SymbolSerializer

class SymbolLimitedListView(generics.ListAPIView):
    queryset = Symbol.objects.all().filter(approved=True).filter(symbol_type="monument") #.filter(pk__lt=961)
    serializer_class = SymbolLimitedSerializer

class HonoreeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Honoree.objects.all()
    serializer_class = HonoreeSerializer

class ContactViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
# Create your views here.
from symbols.models import * 
from rest_framework import viewsets, generics
from symbols.serializers import *



class SymbolDetailView(generics.RetrieveAPIView):
    lookup_field = 'pk'
    queryset = Symbol.objects.all()
    serializer_class = SymbolSerializer

class SymbolZipListView(generics.ListAPIView):
    serializer_class = SymbolSerializer

    def get_queryset(self): 
    	zip_code = self.kwargs['zip_code']
    	return Symbol.objects.filter(zip_code=zip_code)

class SymbolLimitedListView(generics.ListAPIView):
    queryset = Symbol.objects.all()
    serializer_class = SymbolLimitedSerializer

class HonoreeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Honoree.objects.all()
    serializer_class = HonoreeSerializer

class ContactViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
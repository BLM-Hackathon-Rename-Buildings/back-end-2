from django.contrib import admin

from .models import *


class SymbolAdmin(admin.ModelAdmin):
    list_display = ('name','city','state',)
    list_filter = ('approved',)

admin.site.register(Contact)
admin.site.register(Honoree)
admin.site.register(Symbol, SymbolAdmin)

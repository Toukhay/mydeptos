from django.contrib import admin
from .models import User, Location, Contract, Apartments, RealEstateAgency
# Registra la clase User en el admin de Django si es necesario
admin.site.register(User)
admin.site.register(Location)
admin.site.register(Contract)
admin.site.register(Apartments)
admin.site.register(RealEstateAgency)

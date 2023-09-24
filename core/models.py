from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField(default=15)
    address = models.CharField(max_length=100)
    
    #se crea un metodo especial, me permite mostrar algo en el interfaz 
    def __str__(self) :
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=100)

class Contract(models.Model):
    contract_start_date = models.DateField()
    contract_end_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Apartments(models.Model):
    address = models.CharField(max_length=100)
    rooms = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    location= models.ForeignKey(Location, on_delete=models.CASCADE)

class RealEstateAgency(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.IntegerField(default=15)
    email = models.EmailField(max_length=100)
    inmobiliaria=models.ForeignKey(Apartments, on_delete=models.CASCADE)
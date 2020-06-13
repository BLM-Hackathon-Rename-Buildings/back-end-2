from django.db import models


SYMBOL_TYPES = (
    ('body_of_water','body_of_water'), 
    ('bridge','bridge'), 
    ('building','building'), 
    ('city','city'), 
    ('college','college'), 
    ('commemorative_license_plate','commemorative_license_plate'), 
    ('county','county'), 
    ('flag','flag'), 
    ('highway_or_roadway','highway_or_roadway'), 
    ('holiday_or_observances','holiday_or_observances'), 
    ('marker','marker'), 
    ('military_Base','military_Base'), 
    ('monument','monument'), 
    ('other','other'), 
    ('park','park'), 
    ('plaque','plaque'), 
    ('scholarship','scholarship'), 
    ('school','school'), 
    ('seal','seal'), 
    ('song','song'), 
)

class Honoree(models.Model): 
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    photo = models.ImageField(null=True)


class Contact(models.Model): 
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=100)
    email=models.EmailField()
    phone_number=models.CharField(max_length=15)

    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    county=models.CharField(max_length=50)

# Create your models here.
class Symbol(models.Model): 
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=5, null=True)

    latitude = models.DecimalField(max_digits=11, decimal_places=9)
    longitude = models.DecimalField(max_digits=12, decimal_places=9)

    symbol_type = models.CharField(max_length=30,choices=SYMBOL_TYPES)

    petition_link = models.CharField(max_length=100, blank=True, default="")

    approved = models.BooleanField(default=False)
    removed = models.BooleanField(default=False)

    photo = models.ImageField(null=True)

    contacts = models.ManyToManyField(Contact)
    honoree = models.ForeignKey(Honoree, on_delete=models.PROTECT, null=True)




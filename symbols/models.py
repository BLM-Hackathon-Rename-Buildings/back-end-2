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
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    photo = models.ImageField(null=True)

    def __str__(self):
        return self.name


class Contact(models.Model): 
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=100)
    email=models.EmailField()
    phone_number=models.CharField(max_length=15)

    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    county=models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def to_dict(self): 
        data_dict = {}

        data_dict["name"]=self.name
        data_dict["title"]=self.title
        data_dict["email"]=self.email
        data_dict["phone_number"]=self.phone_number

        return data_dict

# Create your models here.
class Symbol(models.Model): 
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=5, blank=True)

    latitude = models.DecimalField(max_digits=11, decimal_places=9)
    longitude = models.DecimalField(max_digits=12, decimal_places=9)

    symbol_type = models.CharField(max_length=30,choices=SYMBOL_TYPES)

    petition_link = models.CharField(max_length=100, blank=True, default="")

    approved = models.BooleanField(default=False)
    removed = models.BooleanField(default=False)

    photo = models.ImageField(null=True)

    contacts = models.ManyToManyField(Contact)
    honoree = models.ForeignKey(Honoree, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return ("{0} — {1}, {2}".format(self.name, self.city, self.state))

    def to_dict(self): 
        data_dict= {}

        data_dict["id"] = self.pk

        data_dict["name"] = self.name
        data_dict["city"] = self.city
        data_dict["state"] = self.state 
        data_dict["county"] = self.county 
        data_dict["latitude"] = self.latitude 
        data_dict["longitude"] = self.longitude
        data_dict["symbol_type"] = self.symbol_type 
        data_dict["petition_link"] = self.petition_link
        data_dict["photo"] = self.photo 
        
        data_dict["contacts"] = [c.to_dict() for c in self.contacts.all()]
        if self.honoree: 
            data_dict["honoree"] = self.honoree.name 

        return data_dict







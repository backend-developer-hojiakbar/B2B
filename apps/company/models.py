from django.db import models
from apps.core.models import BaseModel
# Create your models here.


class Country(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class Company(BaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)
    company_name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, models.CASCADE, related_name='country')

    def __str__(self):
        return str(self.first_name)


class Product(BaseModel):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='products')
    description = models.TextField()
    country = models.ForeignKey(Country, models.CASCADE)
    company = models.ForeignKey(Company, models.CASCADE)

    def __str__(self):
        return str(self.name)


class Category(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Articles(BaseModel):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='articles')
    category = models.ForeignKey(Category, models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return str(self.name)


class Quote(BaseModel):
    OneTimeRequest = 'O'
    Recurring = 'R'
    Dealer = 'D'
    Manufacturer = 'M'
    ServiceProvider = 'S'
    Wholesaler = 'W'
    Requirement_type = [
        (OneTimeRequest, 'OneTimeRequest'),
        (Recurring, 'Recurring')
    ]
    SupplierType = [
        (Dealer, 'Dealer'),
        (Manufacturer, 'Manufacturer'),
        (ServiceProvider, 'ServiceProvider'),
        (Wholesaler, 'Wholesaler')
    ]
    product = models.ForeignKey(Product, models.CASCADE)
    longitude = models.CharField(max_length=60)
    latitude = models.CharField(max_length=60)
    amount = models.PositiveIntegerField(default=0)
    requirement_type = models.CharField(
        max_length=50, choices=Requirement_type, default=OneTimeRequest)
    supplierType = models.CharField(
        max_length=50, choices=SupplierType, default=Dealer)
    requestText = models.TextField()
    img = models.ImageField(upload_to='request img')
    email = models.EmailField()

    def __str__(self):
        return str(self.product)




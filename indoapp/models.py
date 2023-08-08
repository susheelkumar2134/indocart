from django.db import models

# Create your models here.
class IndoUsers(models.Model):
    FirstName=models.CharField(max_length=20)
    LastName=models.CharField(max_length=20)
    Email=models.EmailField(max_length=50)
    Age=models.IntegerField()
    Password=models.CharField(max_length=20)
    class Meta:
        db_table = 'IndoUsers'
        
ProductsCategoryChoices=(('Mobile','Mobile'),
                 ('Camera','Camera'),
                 ('Neckband','Neckband'),
                 ('Tablet','Tablet'),
                 ('TV','TV'),
                 ('Earphone','Earphone'),
                 ('Printer','Printer'),
                 ('Headphone','Headphone'),
                 ('Watch','Watch'),
                 ('CPU','CPU'),
                 ('Mouse','Mouse'),
                 ('Keyboard','Keyboard'))  

ProductsBrandChoices=(('HP','HP'),
                      ('DELL','DELL'),
                      ('Apple','Apple'),
                      ('Samsung','Samsung'),
                      ('Realme','Realme'),
                      ('Redmi','Redmi'),
                      ('LG','LG'),
                      ('Sony','Sony'),
                      ('Motorola','Motorola'),
                      ('Zebronics','Zebronics'))

class Products(models.Model):
    ProductName=models.CharField(max_length=20)
    ProductDetails=models.TextField()
    ProductPrice=models.FloatField()
    ProductCategory=models.CharField(choices=ProductsCategoryChoices,max_length=20)
    ProductImage=models.ImageField()
    ProductBrand=models.CharField(choices=ProductsBrandChoices,max_length=20)
    
    
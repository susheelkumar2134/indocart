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
    ProductImage=models.ImageField(upload_to='Products_images')
    ProductBrand=models.CharField(choices=ProductsBrandChoices,max_length=20)
    
    def _str_(self):
        return self.id
    
STATE_CHOICES= (
    ('Andaman & Nicobar Islands','Andaman & Nicobar Islands'),
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunanchal Pradesh','Arunanchal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chandighar','Chandighar'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Dadar & Nagar Haveli','Dadar & Nagar Haveli'),
    ('Daman and Diu','Daman and Diu'),
    ('Delhi','Delhi'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'),
    ('Himachal','Himachal'),
    ('Jammu & kashmir','Jammu & kashmir'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Lakshadweep','Lakshadweep'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharastra','Maharastra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Puducherry','Puducherry'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Telangana','Telangana'),
    ('Tripura','Tripura'),
    ('Uttarakhand','Uttarakhand'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('West Bengal','West Bengal'),
)   

class DeliveryDetails(models.Model):
    user = models.IntegerField()
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=50)
    
    def _str_(self):
        return str(self.id)

# class Delivery(models.Model):
#     user = models.ForeignKey(IndoUsers, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200)
#     locality = models.CharField(max_length=200)
#     city = models.CharField(max_length=50)
#     zipcode = models.IntegerField()
#     state = models.CharField(choices=STATE_CHOICES,max_length=50)
    
#     def _str_(self):
#         return str(self.id)
    
class Cart(models.Model):
    user = models.IntegerField()
    product = models.IntegerField()
    quantity = models.PositiveIntegerField(default=1)
    
    def _str_(self):
        return str(self.id)
    
class KartProducts(models.Model):
    user = models.IntegerField()
    product = models.IntegerField()
    quantity = models.PositiveIntegerField(default=1)
    ProductName=models.CharField(max_length=20)
    ProductDetails=models.TextField()
    ProductPrice=models.FloatField()
    ProductCategory=models.CharField(choices=ProductsCategoryChoices,max_length=20)
    ProductImage=models.ImageField(upload_to='Products_images')
    
    
ORDER_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the way','On the way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
)

class OrderPlaced(models.Model):
    user = models.CharField(max_length=20)
    customer = models.CharField(max_length=20)
    product = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,default='Pending',choices=ORDER_CHOICES)
    
class PlacedOrder(models.Model):
    user = models.CharField(max_length=20)
    customer = models.CharField(max_length=20)
    product = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField(default=1)
    ProductName=models.CharField(max_length=20)
    ProductDetails=models.TextField()
    ProductPrice=models.FloatField()
    ProductCategory=models.CharField(choices=ProductsCategoryChoices,max_length=20)
    ProductImage=models.ImageField(upload_to='Products_images')
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,default='Pending',choices=ORDER_CHOICES)
from django.db import models

from django.conf import settings

# Create your models here.
class login(models.Model):
    Name=models.CharField(default="", max_length=50)
    Email=models.EmailField(default="", max_length=254)
    Username=models.CharField(default="",max_length=5)
    Password=models.CharField(default="", max_length=50)
    
class enquiry(models.Model):
    EName=models.CharField(default="",max_length=50)
    Mail=models.CharField(default="",max_length=50)
    YourMessage=models.CharField(default="",max_length=300)




from django.db import models
from django.conf import settings



class Booking(models.Model): 
    email=models.EmailField(default='default@example.com')
    CarBrand=models.CharField(default="carname", max_length=50)
    ModelName=models.CharField(default="modelname", max_length=50)

    phone = models.CharField(max_length=10, default="91")
    date = models.DateField()  
    address=models.CharField(default="",max_length=300)

    



    SERVICE_CATE = [
        ('1', 'General Service'),
        ('2', 'Painting Service'),
        ('3', 'AC Service'),
        ('4', 'Detailing Service'),
        ('5', 'Custom Repair Service'),
        ('6', 'Insurance'),
    ]
    service_category = models.CharField(choices=SERVICE_CATE, default="service category",max_length=10)
  
    SLOT_CHOICES = [
        (1, '10.00am-1.00pm'),
        (2, '3.00pm-5.00pm'),  
    ]

    pickup_slot = models.IntegerField(choices=SLOT_CHOICES, default="select time pickup slot") 



  
    
    package = models.CharField(max_length=255, null=True, blank=True)
    
    booked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
      constraints = [
        models.UniqueConstraint(fields=['date', 'pickup_slot'], name='unique_booking_per_slot')
    ]
    
    def __str__(self):
        return f"{self.CarBrand}-{self.ModelName} - {self.date} -{self.phone} -{self.address}at {self.pickup_slot}"





 
 

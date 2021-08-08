from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    relation = models.CharField(max_length=100,blank=True,null=True)
    email = models.EmailField(max_length=222,blank=True,null=True)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.full_name
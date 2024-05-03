from django.db import models

# Create your models here.



class ContactUs(models.Model):
    sender_firstname = models.CharField(max_length=100)
    sender_lastname = models.CharField(max_length=100)
    sender_email = models.EmailField(max_length=100)
    message = models.CharField(max_length=1000)
    come_time = models.DateTimeField()

    def __str__(self):
        return self.sender_email
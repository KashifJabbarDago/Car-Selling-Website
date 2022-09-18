from django.db import models

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=150)
    msg = models.TextField()
    def __str__(self):
        return self.name

class SignUp(models.Model):
    username = models.CharField(max_length=150)
    fname = models.CharField(max_length=150)
    lname = models.CharField(max_length=150)
    email_check = models.CharField(max_length=100)
    pass1 = models.CharField(max_length=100)
    pass2 = models.CharField(max_length=100)



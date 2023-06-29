from django.db import models

# Create your models here.


class Addmision(models.Model):
    name = models.CharField(("Name"), max_length=250)
    phono = models.CharField(("Mobile Number"), max_length=250)
    email = models.CharField(("Email"), max_length=250)
    state = models.CharField(("State"), max_length=250)
    course = models.CharField(("Course"), max_length=250)


    def __str__(self):
        return self.name
    
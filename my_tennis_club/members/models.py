from django.db import models

# Create your models here.
class Members(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    rollno = models.IntegerField(null=True)
    dob = models.DateField(null=True)
    slug = models.SlugField(default="", null=False)


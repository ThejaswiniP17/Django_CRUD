from django.db import models

class Animal(models.Model):
    aname = models.CharField(max_length=100, null=True, blank=True)  # Name is required
    animal_type = models.CharField(max_length=50, null=True, blank=True)
    afood = models.CharField(max_length=100, null=True, blank=True)
    ahabitat = models.CharField(max_length=100, null=True, blank=True)
    acolor = models.CharField(max_length=100, null=True, blank=True)
    aspecial_abilities = models.CharField(max_length=200, null=True, blank=True)  # Increased max length for details
    # aimage=models.ImageField(upload_to='images/',null=True,blank=True)
    aimage = models.ImageField(upload_to='images/', null=True, blank=True, default='images/all animalsss.jpg')


    def __str__(self):
        return self.aname

from django.db import models

# Create your models here.

class Bird(models.Model):
    bname=models.CharField(max_length=100)
    bfood=models.TextField()
    bScientificName=models.CharField(max_length=200,null=True, blank=True)
    bHabitat=models.CharField(max_length=100,null=True, blank=True)
    bMigrationPattern=models.CharField(max_length=200,null=True, blank=True)
    bimg=models.ImageField(upload_to='images/',blank=True,null=True)

    # bDateAdded=models.DateTimeField (auto_now_add=True)
    
    def _str_(self):
        return self.bnam



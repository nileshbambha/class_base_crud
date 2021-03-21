from django.db import models

# Create your models here.
class emp(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    choices = (
        ('Male' , 'M'),
        ('Female' , 'F')
    )
    gender = models.CharField(choices = choices,max_length=50)
    image = models.ImageField(upload_to='img')
    
    def __str__(self):
        return self.name

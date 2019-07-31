from django.db import models

# Create your models here.
class Plan(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    validity = models.IntegerField()
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    class Meta:
        ordering =('price',)
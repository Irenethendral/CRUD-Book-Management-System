from django.db import models

class Book(models.Model):
   title=models.CharField(max_length=100, blank=True, null=True)
   author=models.CharField(max_length=100)
   price=models.IntegerField()
   
def _str_(self):
    return self.ttle
   

from django.db import models

from django.db import models

class Book(models.Model):
    name=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    language=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    genre=models.CharField(max_length=200)
    yearofpublication=models.PositiveIntegerField()


    def __str__(self):
        return self.name
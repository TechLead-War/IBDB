from django.db import models

# Create your models here.


# if someone access any object of <name> then what name of that object should be returned.
class Movie(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=1000)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

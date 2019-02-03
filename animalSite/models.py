from django.db import models

class Animal(models.Model):
    animal_name = models.CharField(max_length=100)
    def __str__(self):
        return self.animal_name


class Description(models.Model):
    animal = models.OneToOneField(
        Animal,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    food = models.TextField()
    habitat = models.TextField()
    legs = models.IntegerField(default=4)
    def __str__(self):
        return self.food+" "+self.habitat+" "+str(self.legs)

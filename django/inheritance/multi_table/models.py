from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} | {self.address}'


class Restaurant(models.Model):
    server_hot_gods = models.BooleanField(default=False)
    server_pizza = models.BooleanField(default=False)

    def __str__(self):
        return f'Restaturant {self.name} | {self.address}'

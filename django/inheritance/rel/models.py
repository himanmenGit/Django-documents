from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Item(models.Model):
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)ss',
        related_query_name='%(app_label)s_%(class)s',
        # related_query_name='item',
    )

    class Meta:
        abstract = True


class Fruit(Item):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Food(Item):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

from django.db import models
from django.db.models import Manager


class Person(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class NewManager(Manager):
    def get_queryset(self):
        print('NewManger get_queryset')
        return super().get_queryset()


class MyPerson1(Person):
    secondary = NewManager()

    class Meta:
        proxy = True


class ExtraManagerModel(models.Model):
    secondary = NewManager()

    class Meta:
        abstract = True


class MyPerson2(Person, ExtraManagerModel):
    class Meta:
        proxy = True

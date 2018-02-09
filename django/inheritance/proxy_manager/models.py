from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class NewManager(models.Model):
    def get_queryset(self):
        print('NewManger get_queryset')
        return super().get_queryset()


class ExtraManagerModel(models.Model):
    secondary = NewManager()

    class Meta:
        abstract = True


class MyPerson1(Person):
    secondary = NewManager()

    class Meta:
        proxy = True


class MyPerson2(Person, ExtraManagerModel):
    class Meta:
        proxy = True

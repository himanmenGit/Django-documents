from django.db import models


class Car(models.Model):
    manufacturer = models.ForeignKey(
        'Manufacturer',
        on_delete=models.CASCADE,
        verbose_name='제조사',
    )
    name = models.CharField('모델명', max_length=60)

    def __str__(self):
        return '{manufacturer} {car_name}'.format(
            manufacturer=self.manufacturer.name,
            car_name=self.name
        )


class Manufacturer(models.Model):
    name = models.CharField('제조사명', max_length=50)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=60)
    teacher = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(primary_key=True, max_length=60)

    def __str__(self):
        return f'{self.name}'


class Pokemon(models.Model):
    dex_number = models.IntegerField(primary_key=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.dex_number:03}. {self.name} ({self.type.name})'

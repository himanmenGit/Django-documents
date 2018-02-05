from django.contrib import admin

from foreignkey.models import Manufacturer, Car

admin.site.register(Manufacturer)
admin.site.register(Car)
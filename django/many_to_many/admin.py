from django.contrib import admin

from many_to_many.models import Topping, Pizza

admin.site.register(Topping)
admin.site.register(Pizza)
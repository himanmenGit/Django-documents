from django.contrib import admin

from many_to_many.models import Topping, Pizza, Post, User, PostLike

admin.site.register(Topping)
admin.site.register(Pizza)

admin.site.register(Post)
admin.site.register(User)
admin.site.register(PostLike)
from django.db import models

__all__ = [
    'FacebookUser',
]


class FacebookUser(models.Model):
    name = models.CharField(max_length=50)
    # 자기 자신도 facebookUser이기 때문에 self로 참조.
    friends = models.ManyToManyField('self')

    def __str__(self):
        return self.name

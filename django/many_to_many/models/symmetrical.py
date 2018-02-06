from django.db import models

__all__ = [
    'InstagramUser',
]


class InstagramUser(models.Model):
    name = models.CharField(max_length=50)
    following = models.ManyToManyField(
        'self',
        # 대칭 관계가 아님
        symmetrical=False,
        related_name='get_followers',
    )

    def __str__(self):
        followings_string = ', '.join(self.following.values_list('name', flat=True))

        return '{name} (팔로워: {friends})'.format(
            name=self.name,
            friends=followings_string,
        )

    def followers(self):
        # 자신을 following 하고 있는 사람들을 리턴
        # 문자열이 아닌 쿼리 자체
        # return self.InstagramUser.set.all()
        return self.get_followers.all()

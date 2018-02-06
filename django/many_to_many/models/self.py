from django.db import models

__all__ = [
    'FacebookUser',
]


class FacebookUser(models.Model):
    name = models.CharField(max_length=50)
    # 자기 자신도 facebookUser이기 때문에 self로 참조.
    friends = models.ManyToManyField('self')

    class Meta:
        verbose_name_plural = 'Self - FacebookUsers'

    def __str__(self):
        # name이 '이한영' 이며
        # 친구로 '박보영', '아이유'를 가지는 경우
        # 이한영 (친구: 박보영, 아이유)

        # return_str = f'{self.name} (친구:'
        # for friend in self.friends.all():
        #     return_str += friend.name + ', '
        # return_str = return_str[:-2]
        # return_str += ')'
        # return return_str

        # list comprehension
        # friends_string = ', '.join([friend.name for friend in self.friends.all()])

        # Managet의 values_list를 사용
        # DB에서 모든 friend의 'name'값 만 가져옴
        friends_string = ', '.join(self.friends.values_list('name', flat=True))

        return '{name} (친구: {friends})'.format(
            name=self.name,
            friends=friends_string,
        )
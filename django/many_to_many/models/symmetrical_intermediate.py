from django.db import models

__all__ = [
    'TwitterUser',
    'Relation',
]


class TwitterUser(models.Model):
    """
    내가 A를 follow 함
        나는 A의 follower
        A는 나의 followee

    A와 내가 서로 follow함
        나와 A는 friend

    Block기능이 있어야 함

    """
    name = models.CharField(max_length=50)
    relations = models.ManyToManyField(
        'self',
        symmetrical=False,
        through='Relation',
        related_name='+',
    )

    # def __str__(self):
    #     relations_string = ', '.join(self.relations.values_list('name', flat=True))
    #     # block_string = ', '.join(self.relations.values_list('b', flat=True))
    #     return '{name} (팔로워: {friends}) (블럭: {block}'.format(
    #         name=self.name,
    #         friends=relations_string,
    #         # block=block_string,
    #     )


class Relation(models.Model):
    """
    유저간의 관계를 정의하는 모델
    """
    RELATION_TYPE_FOLLOWING = 'f'
    RELATION_TYPE_BLOCK = 'b'
    CHOICES_TYPE = (
        (RELATION_TYPE_FOLLOWING, '팔로잉'),
        (RELATION_TYPE_BLOCK, '차단'),
    )
    from_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        # 자신이 from_user인 경우에 Relation목록을 가져오고 싶을 경우
        related_name='relations_by_from_user',
    )
    to_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        # 자신이 to_user인 경우 Relation목록을 가져오고 싶을 경우
        related_name='relations_by_to_user',
    )
    type = models.CharField(max_length=1, choices=CHOICES_TYPE)


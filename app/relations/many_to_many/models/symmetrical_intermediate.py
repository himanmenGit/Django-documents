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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Symmetrical_Intermediate - TwitterUsers'

    @property
    def following(self):
        """
        내가 follow하고 있는 TwitterUser목록을 가져옴
        :return:
        """

        # 내가 from_user이며, type이 팔로잉인 Relation의 쿼리셋
        following_relations = self.relations_by_from_user.filter(type=Relation.RELATION_TYPE_FOLLOWING)
        # 위에서 정제한 쿼리셋에서 'to_user'값만 리스트로 가져옴 (내가 팔로잉 하는 유저의 to_user 리스트)
        following_pk_list = following_relations.values_list('to_user', flat=True)
        # TwitterUser테이블에서 pk가
        # 바로 윗줄에서 만든 following_pk_list (내가 팔로잉하는 유저의 pk리스트)
        #   에 포함되는 User목록을 following_users변수로 할당
        following_users = TwitterUser.objects.filter(pk__in=following_pk_list)
        return following_users

    @property
    def followers(self):
        pk_list = self.relations_by_to_user.filter(
            type=Relation.RELATION_TYPE_FOLLOWING).values_list('from_user', flat=True)
        return TwitterUser.objects.filter(pk__in=pk_list)

    @property
    def block_users(self):
        """
        내가 block하고 있는 TwitterUser목록을 가져옴
        :return:
        """

        # block_relations = self.relations_by_from_user.filter(type=Relation.RELATION_TYPE_BLOCK)
        # block_pk_list = block_relations.values_list('to_user', flat=True)
        # block_users = TwitterUser.objects.filter(pk__in=block_pk_list)
        # return block_users

        pk_list = self.relations_by_from_user.filter(
            type=Relation.RELATION_TYPE_BLOCK).values_list('to_user', flat=True)
        return TwitterUser.objects.filter(pk__in=pk_list)

    def is_followee(self, to_user):
        """
        내가 to_user를 follow하고 있는지 여부를 True/False로 반환
        :param to_user:
        :return:
        """
        # pk_list = self.relations_by_from_user.filter(
        #     type=Relation.RELATION_TYPE_FOLLOWING).values_list('to_user', flat=True)
        # if to_user.pk in pk_list:
        #     return True
        # return False

        return self.following.filter(pk=to_user.pk).exists()

    def is_follower(self, from_user):
        """
        from_user가 나를 follow하고 있는지 여부를 True/False로 반환
        :param from_user:
        :return:
        """
        # pk_list = self.relations_by_to_user.filter(
        #     type=Relation.RELATION_TYPE_FOLLOWING).values_list('from_user', flat=True)
        # if from_user.pk in pk_list:
        #     return True
        # return False

        return self.followers.filter(pk=from_user.pk).exists()

    def follow(self, to_user):
        """
        to_user에 주어진 TwitterUser를 follow함
        :param to_user:
        :return:
        """
        self.relations_by_from_user.filter(to_user=to_user).delete()
        self.relations_by_from_user.create(
            to_user=to_user,
            type=Relation.RELATION_TYPE_FOLLOWING,
        )

        # Relation.objects.create(
        #     from_user=self,
        #     to_user=to_user,
        #     type=Relation.RELATION_TYPE_FOLLOWING,
        # )

    def block(self, to_user):
        """
        to_user에 주어진 TwitterUser를 block함
        :param to_user:
        :return:
        """
        self.relations_by_from_user.filter(to_user=to_user).delete()
        self.relations_by_from_user.create(
            to_user=to_user,
            type=Relation.RELATION_TYPE_BLOCK,
        )


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
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Symmetrical_Intermediate - Relations'
        unique_together = (
            # from_user와 to_user의 값이 이미 있을 경우
            # DB에 중복 데이터 저장을 막음
            # ex) from_user가 1, to_user가 3인 데이터가 이미 있다면
            #       두 항목의 값이 모두 같은 또 다른 데이터가 존재할 수 없음
            ('from_user', 'to_user')
        )

from datetime import datetime
from django.utils import timezone

from django.db import models


class Topping(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=50)
    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        return self.name


# Extra fiels on many-to-many relationships
class Post(models.Model):
    title = models.CharField(max_length=50)
    like_users = models.ManyToManyField(
        'User',
        through='PostLike',
        # MTM으로 연결된 반대편에서
        # (지금의 경우 특정 User가 좋아요 누른 Post목록을 가져오고 싶은 경우)
        # 자동 생성되는 역방향 매니저 이름인 post_set대신
        # related_name으로 변경하여 사용한다.
        related_name='like_posts',
    )

    def __str__(self):
        return self.title


class User(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # 글 title이 "공지사항이며 유저name이 "이한영"이고,
        # 좋아요 누른 시점이 2018.01.31일떄
        # "공지사항"글의 좋아요(이한영, 2018.01.31) 으로 출력
        return '"{title}"글의 좋아요({name}, {date})'.format(
            title=self.post.title,
            name=self.user.name,
            date=datetime.strftime(
                # timezone.make_naive(self.created_date), '%y.%m.%d'
                timezone.localtime(self.created_date),'%y.%m.%d'
            )
        )

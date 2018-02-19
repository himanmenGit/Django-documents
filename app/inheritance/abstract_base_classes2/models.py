from django.db import models


class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True


class Student(CommonInfo):
    home_group = models.CharField(max_length=5)


# Be careful with related_name and related_query_na
class Other(models.Model):
    pass


class Base(models.Model):
    other = models.ForeignKey(Other,
                              on_delete=models.CASCADE,
                              # 추상클래스를 쓸때
                              # 자식 모델 클래스가 여럿 이면
                              # related_name이 같으면 충돌 한다.
                              related_name='%(app_label)s_%(class)s_set',
                              related_query_name='%(app_label)s_%(class)s',
                              )

    class Meta:
        abstract = True


class ChildA(Base):
    pass


class ChildB(Base):
    pass

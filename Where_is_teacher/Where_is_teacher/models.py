import datetime

from django.db import models


class Teacher(models.Model):
    """
    Teacherモデルは、教員の名前、編集者、メッセージ、更新時間、状態を保持するためのモデルクラスです。
    このクラスは、DjangoのModelクラスを継承しています。
    """

    # 名前
    name = models.CharField(verbose_name = 'name', max_length=20)

    # 編集者
    contributor = models.CharField(verbose_name = 'contributor', max_length=20)

    # メッセージ
    text = models.TextField(verbose_name = 'comment', max_length=1000)

    # 更新時間
    time = models.DateTimeField(verbose_name = 'update time')

    STATE_CHOICES = (
        (0, '不明'),
        (1, '在室'),
        (2, '不在')
    )

    # 状態
    state = models.IntegerField(
        verbose_name = 'state',
        choices = STATE_CHOICES
        )    

class Sort(models.Model):
    """
    Sortモデルは、教員の情報を表示する際の並べ替え方法を保持するためのモデルクラスです。
    このクラスは、DjangoのModelクラスを継承しています。
    """
    SORT_CHOICES = (
        (0, 'なし'),
        (1, '学科別'),
        (2, '五十音')
    )
    sort = models.IntegerField(
        verbose_name = 'sort',
        choices = SORT_CHOICES,
        default = 0
        )

    def __str__(self):
        return self.name

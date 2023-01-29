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

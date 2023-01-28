from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm

from .models import Teacher

class LoginForm(AuthenticationForm):
    """
    LoginFormクラスは、認証用ログインフォームを表示するためのクラスです。
    このクラスは、DjangoのAuthenticationFormクラスを継承しています。
    init()メソッドは、フォームの各フィールドのウィジェットにplaceholder属性を設定するための
    オーバーライドメソッドです。
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label

class TeacherForm(ModelForm):
    """
    TeacherFormクラスは、教員の情報を入力、管理するためのフォームを表示するためのクラスです。
    このクラスは、DjangoのModelFormクラスを継承しています。
    Metaクラスは、このフォームが対応するモデルクラスや、このフォームに表示するフィールド、
    フィールドに表示するラベルを指定するためのクラスです。
    """
    class Meta:
        model = Teacher
        fields = ['name', 'state', 'text', 'time']
        labels = {
            'name': '名前',
            'state': '状態',
            'text': 'コメント',
            'time': '更新時刻'
            }

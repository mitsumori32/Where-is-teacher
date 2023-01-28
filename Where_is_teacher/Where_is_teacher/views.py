from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import json

from .models import Teacher, Sort
from .forms import LoginForm, TeacherForm


class IndexView(View):
    """
    IndexViewクラスは、Where_is_teacherアプリケーションの
    トップページを表示するためのクラスです。
    get()メソッドは、指定されたtemplate_nameで指定された
    HTMLテンプレートを使用して、レンダリングした結果を
    HTTPクライアントに返します。
    """
    template_name = 'Where_is_teacher/index.html'
    context_object_name = 'teacher_list'

    def get_context_data(self, **kwargs):
        """
        このメソッドは、HTMLテンプレートで使用するコンテキストデータを
        生成するために呼び出されます。
        生成されるコンテキストデータには、sort_listというキーがあり、
        その値はSortモデルのすべてのオブジェクトが入ったクエリセットです。
        """
        context = super(IndexView, self).get_context_data(**kwargs)
        tmp = {
            'sort_list': Sort.objects.all()
        }
        context.update(tmp)
        return context
    
    def get_queryset(self):
        return super().get_queryset(**kwargs)

    def get(self, request):
        """
        このメソッドは、HTTPクライアントからのGETリクエストを処理します。
        テンプレートに渡すためのデータを生成し、render()関数を呼び出して
        生成されたHTMLを返します。
        """
        data = json.dumps(
                list(map(lambda t:
                         {'name': t.name, 'contributor': t.contributor, 'text': t.text, 'time': str(t.time), 'state': t.state, 'id': t.id}, Teacher.objects.all())), ensure_ascii=False)

        print(data[65:70])
        
        params = {
            "title": "Where is teacher !!",
            "teacher_list": Teacher.objects.all(),
            "json_data": data,
            }

        return render(request, self.template_name, params)

class DetailView(View):
    """
    DetailViewクラスは、教員の情報詳細ページを表示するためのクラスです。
    get()メソッドは、指定されたtemplate_nameで指定されたHTMLテンプレートを使用して、
    レンダリングした結果をHTTPクライアントに返します。
    """
    template_name = 'Where_is_teacher/detail.html'
    context_object_name = 'teacher_list'

    def get(self, request, teacher_id):
        """
        このメソッドは、HTTPクライアントからのGETリクエストを処理します。
        テンプレートに渡すためのデータを生成し、render()関数を呼び出して
        生成されたHTMLを返します。
        """
        params = {
            "title" : "Where is teacher !!",
            "teacher_list": Teacher.objects.all(), # idを含むTeacherモデルの全ての情報をteacher_listに格納
            "teacher_id": teacher_id # getした教員の情報（id） これを用いて教員の識別を行う
            }

        return render(request, self.template_name, params)

class TeacherView(LoginRequiredMixin, View):
    """
    TeacherViewクラスは、ログインしている教員が自身の情報を管理するためのクラスです。
    get()メソッドは、教員の情報を元にフォームを作成し、HTMLテンプレートを使用して
    レンダリングした結果をHTTPクライアントに返します。
    post()メソッドは、HTTPクライアントから送信されたフォームデータを元に、
    教員の情報を更新します。
    """
    template_name = 'Where_is_teacher/teacher.html'
    context_object_name = 'teacher_list'
    login_url= template_name

    def post(self, request):
        """
        このメソッドは、HTTPクライアントからのPOSTリクエストを処理します。
        リクエストから送信されたフォームデータを元に、教員の情報を更新します。
        その後、テンプレートに渡すためのデータを生成し、render()関数を呼び出して
        生成されたHTMLを返します。
        """
        teacher = Teacher.objects.get(id=request.user.id)
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()

        params = {"title": "Where is teacher !!",
                  "teacher_list": Teacher.objects.all(),
                  "teacher_form": form,
                  "message": 'POST'}

        return render(request, self.template_name, params)

    def get(self, request):
        """
        このメソッドは、HTTPクライアントからのGETリクエストを処理します。
        教員の情報を元にフォームを作成し、テンプレートに渡すためのデータを生成し、
        render()関数を呼び出して、生成されたHTMLを返します。
        """
        queryset = Teacher.objects.get(id=request.user.id)
        init_data = {
            'name': queryset.name,
            'state': queryset.state,
            'text': queryset.text,
            'time': queryset.time,
            }
        form = TeacherForm(initial=init_data)

        params = {"title": "Where is teacher !!",
                  "teacher_list": Teacher.objects.all(),
                  "teacher_form": form,
                  "message": 'GET'}

        return render(request, self.template_name, params)

class LoginView(LoginView):
    template_name = 'Where_is_teacher/login.html'
    form_class = LoginForm

class LogoutView(LogoutView):
    template_name = "Where_is_teacher/logout.html"

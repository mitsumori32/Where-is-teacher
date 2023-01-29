from django.urls import path
from . import views

app_name = 'Where_is_teacher'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('teacher_detail/<int:teacher_id>/', views.DetailView.as_view(), name='detail'),
    path('teachers/login/', views.LoginView.as_view(), name='login'),
    path('teachers/logout/', views.LogoutView.as_view(), name='logout'),
    path('teachers/', views.TeacherView.as_view(), name='teacher'), 
]

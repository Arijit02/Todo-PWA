from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="main-home"),
    path("base/", views.base, name="base-layout"),
    path("offline/", views.offline, name="offline-layout"),
    path("handle-login/", views.handleLogin, name="handle-login"),
    path("todos/<str:username>", views.dashboard, name='todo-home'),
    path("todos/delete/<str:username>/<int:pk>/",
         views.delete, name='todo-delete')
]

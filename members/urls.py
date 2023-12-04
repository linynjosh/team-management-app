from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add_member", views.add_member, name="add_member"),
    path("edit_member", views.edit_member, name="edit_member"),
    path('delete_member', views.delete_member, name='delete_member'),
    ]
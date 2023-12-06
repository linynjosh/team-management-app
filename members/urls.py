from django.urls import path
from . import views
from .views import MemberDeleteView, EditMemberView, AddMemberView, MemberListView

urlpatterns = [
    path("", MemberListView.as_view(), name="home"),
    path("add_member", AddMemberView.as_view(), name="add_member"),
    path('edit_member/<str:first_name>/<str:last_name>/', EditMemberView.as_view(), name='edit_member'),
    path('delete_member', MemberDeleteView.as_view(), name='delete_member'),
    ]
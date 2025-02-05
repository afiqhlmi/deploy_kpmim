from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("course/", views.course, name="course"),
    path("mentor/", views.mentor, name="mentor"),
    path("search/", views.search, name="search")
]
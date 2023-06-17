from django.urls import path

from . import views

urlpatterns = [
    path("upload-pic/", views.upload_pic, name="upload-pic"),
    path("pic-list/", views.pic_list, name="pic-list"),
]

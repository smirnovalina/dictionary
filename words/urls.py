from django.conf.urls import url
from words import views

urlpatterns = [
    url(r'^words/$', views.WordList.as_view()),
    url(r'^words/(?P<pk>[0-9]+)/$', views.WordDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

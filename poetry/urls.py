from django.conf.urls import url
from . import views
app_name = 'poetry'
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^(?P<poem_id>[0-9]+)/$', views.poemdetail, name = 'poemdetail'),
    url(r'^author/(?P<author_id>[0-9]+)/$', views.authordetail, name = 'authordetail'),
    url(r'^explore/$', views.explore, name = 'explore'),
    url(r'^register/$', views.register, name = 'register'),
    url(r'^login/$', views.user_login, name = 'login'),
    url(r'^logout/$', views.user_logout, name = 'logout'),
    url(r'^account/$', views.account_page, name = 'account'),
    url(r'^favorite/$', views.favorite, name = 'favorite'),
    url(r'^favoriteline/$', views.favoriteline, name = 'favoriteline'),
]

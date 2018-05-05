from django.conf.urls import url
from home.views import HomeView
from . import views
app_name = "home"
urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_friends, name='change_friends'),
    url(r'^post/(?P<pk>\d+)/$',views.single_post , name='single_post'),
]

from django.conf.urls import url
from home.views import HomeView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home')
]

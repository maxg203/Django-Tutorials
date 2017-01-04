from django.conf.urls import url, include
from django.contrib import admin
from tutorial import views


urlpatterns = [
    url(r'^$', views.login_redirect, name='login_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('accounts.urls', namespace='accounts')),
]

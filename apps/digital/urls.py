from django.conf.urls import url
from apps.digital.views import home

urlpatterns = [
    url(r'^$', home, name="home"),
    # url(r'^registrar', RegistroUsuario.as_view(), name="registrar"),
]

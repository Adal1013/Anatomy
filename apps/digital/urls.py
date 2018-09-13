from django.conf.urls import url
from apps.digital.views import home, organo

urlpatterns = [
    url(r'^$', home, name="home"),
    # url(r'^registrar', RegistroUsuario.as_view(), name="registrar"),
    # url(r'^organo/',organo, name="organo"),
    url(r'^organo/(?P<pk>\d+)/$', organo , name='organo')
]

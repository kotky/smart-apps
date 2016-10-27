from django.conf.urls import url
from multimeter import views

urlpatterns = [
    url(r'^api/(?P<pk>[0-9]+)', views.universal_json_container_detail),
    url(r'^api', views.universal_json_container_list),
    url(r'^$', views.index),
]
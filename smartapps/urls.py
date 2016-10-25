from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import multimeter.views

# Examples:
# url(r'^$', 'smartapps.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', multimeter.views.index, name='index'),
    url(r'^db', multimeter.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^multimeter/', include('multimeter.urls')),
]

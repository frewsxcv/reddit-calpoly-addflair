from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from register.views import add

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^reddit/calpoly/register/', add),
    url(r'^reddit/calpoly/admin/', include(admin.site.urls)),
)

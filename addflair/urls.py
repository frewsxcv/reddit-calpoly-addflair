from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from addflair.register.views import add

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', add),
    url(r'^admin/', include(admin.site.urls)),
)

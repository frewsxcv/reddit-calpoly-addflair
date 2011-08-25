from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^add/', 'add_flair.views.add'),
    url(r'^admin/', include(admin.site.urls)),
)

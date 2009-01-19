from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # (r'^sovereignty/', include('sovereignty.foo.urls')),
    (r'^accounts/', include('registration.urls')),
    (r'^avatar/', include('avatar.urls')),
    (r'^admin/(.*)', include(admin.site.urls)),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
)

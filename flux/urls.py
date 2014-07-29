from django.conf import settings
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Api
from tastypie.api import Api
from api.ot_resource import OtResource
from api.field import FieldResource
from api.section import SectionResource
from api.ot_image import OtImageResource

v1_api = Api(api_name='v1')
v1_api.register(OtResource())
v1_api.register(FieldResource())
v1_api.register(SectionResource())
v1_api.register(OtImageResource())



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'flux.views.home', name='home'),
    # url(r'^flux/', include('flux.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'api/', include(v1_api.urls)),
    url(r'', include('webapp.urls')),



)


if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))

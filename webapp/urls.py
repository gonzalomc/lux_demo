# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from webapp.private.views import OtListView
from webapp.private.admin_views import PermissionView, PermissionDetailView
from webapp.private.ot_views import OtDetailView, OtCreateView, OtUpdateView
from webapp.private.client_views import ClientListView
from webapp.private.technical_views import TechnicalListView, TechnicalDetailView, TechnicalCreateView
from webapp.private.product_views import ProductListView, ProductNewView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'flux.views.home', name='home'),
    # url(r'^flux/', include('flux.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
                          {'next_page': '/accounts/login/'}),

    # URL: OTs
    url(r'^ot/$', OtListView.as_view(), name='ot_list'),
    url(r'^ot/nueva/$', OtCreateView.as_view(), name='ot_create'),
    url(r'^ot/(?P<pk>\d+)/$', OtUpdateView.as_view(), name='ot_update'),
    url(r'^ot/(?P<pk>\d+)/detalle/$', OtDetailView.as_view(), name='ot_detail'),

    # URL: Clientes
    url(r'^clientes/$', ClientListView.as_view(), name='client_list'),

    # URL: Técnicos
    url(r'^tecnicos/$', TechnicalListView.as_view(), name='technical_list'),
    url(r'^tecnicos/nuevo/$', TechnicalCreateView.as_view(), name="technical_create"),
    url(r'^tecnicos/(?P<pk>\d+)/$', TechnicalDetailView.as_view(), name='technical_detail'),

    # URL: Productos
    url(r'^productos/$', ProductListView.as_view(), name='product_list'),
    url(r'^productos/nuevo/$', ProductNewView.as_view(), name='product_create'),

    url(r'^panel_admin/', PermissionView.as_view(), name='group_list'),
    url(r'^permisos/(?P<pk>\d+)/$', PermissionDetailView.as_view(), name='group_permissions'),


)
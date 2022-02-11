from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
	url(r'^eox-info$', views.info_view, name='eox-info'),
]

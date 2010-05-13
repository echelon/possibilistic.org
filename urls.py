from django.conf.urls.defaults import *
import os

urlpatterns = patterns('possibilistic.views',
	(r'^/?$', 'index'),
	(r'^about(\.html|/)?$', 'about'),
	(r'^docs/', include('possibilistic.mpages.urls')),
)

# My local server isn't configured to serve static files.
if os.getenv('USERNAME') == 'brandon':

	urlpatterns += patterns('',
		(r'^img/(?P<path>.*)$', 'django.views.static.serve',
			{'document_root': 
			'/home/brandon/Dev/possibilistic.org/public/img/'}),
		(r'^theme/(?P<path>.*)$', 'django.views.static.serve',
			{'document_root': 
			'/home/brandon/Dev/possibilistic.org/public/theme'}),
		(r'^script/(?P<path>.*)$', 'django.views.static.serve',
			{'document_root': 
			'/home/brandon/Dev/possibilistic.org/public/script'}),
	)


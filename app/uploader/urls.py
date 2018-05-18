from django.contrib import admin
from django.conf.urls import include, url
from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import RedirectView


urlpatterns = [
    url(r'^api-manager/', admin.site.urls),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^api/', include('uploader.apps.api.urls')),
    url(r'^', include(('uploader.apps.app.urls', 'uploader'), namespace='app'))
]


from django.contrib import admin
from django.conf.urls import include, url
from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import RedirectView


urlpatterns = [
    url(r'^api-manager/', admin.site.urls),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^api/', include('uploader.apps.api.urls'))
]


if settings.DEBUG:

    from django.conf.urls.static import static
    import debug_toolbar

    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

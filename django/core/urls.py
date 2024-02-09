from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings

urlpatterns = i18n_patterns(

    # General app's urls
    path('', include('general.urls')),

    # Don't show the default language in the URL
    prefix_default_language=False

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

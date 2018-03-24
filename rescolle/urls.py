from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('social_django.urls', 'social'))),
    path('', include(('rescolle_view.views.urls', 'app')))
]

if settings.IS_DEVELOP:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


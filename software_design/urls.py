from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Where_is_teacher/', include('Where_is_teacher.urls')),
]

#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
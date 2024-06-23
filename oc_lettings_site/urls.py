from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from django.conf.urls.static import static
from . import views


urlpatterns = [
    path("", include("home.urls")),
    path("lettings/", include("lettings.urls")),
    path("profiles/", include("profiles.urls")),
    path("admin/", admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = views.custom_404_view
handler500 = views.custom_500_view

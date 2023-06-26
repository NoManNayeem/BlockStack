from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path,re_path

#### API Documentations ########
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


admin.site.site_header = 'Social App Admin'


schema_view = get_schema_view(
   openapi.Info(
      title="Social App API",
      default_version='v1',
      description="Social App Description",
      terms_of_service="website",
      contact=openapi.Contact(email="Contact"),
      license=openapi.License(name="Appropriate License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    # Core URLs
    path('core/', include('core.urls')),
    # API Docs
    re_path(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from accountApp import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.urls.conf import re_path

schema_view = get_schema_view(
    openapi.Info(
        title="Basalt API Document",
        default_version="v1",
        description="Basalt API Description",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="salehzadeh@gmail.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('userApp.urls')),  # Include User app's URLs
    path('account/', include('accountApp.urls')),  # Include Account app's URLs
    path('transaction/', include('transactionApp.urls')),  # Include Transaction app's URLs
    path('', views.index, name='index'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

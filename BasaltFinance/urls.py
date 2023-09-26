from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from accountApp import views
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('userApp.urls')),  # Include User app's URLs
    path('account/', include('accountApp.urls')),  # Include Account app's URLs
    path('transaction/', include('transactionApp.urls')),  # Include Transaction app's URLs
    path('', views.index, name='index'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

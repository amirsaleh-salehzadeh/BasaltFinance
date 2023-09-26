from transactionApp import views, rest_viewsfrom django.urls.conf import path, includefrom drf_yasg.views import get_schema_viewfrom drf_yasg import openapifrom rest_framework import permissionsapp_name = 'transactionApp'schema_view = get_schema_view(    openapi.Info(        title="Basalt API Document",        default_version="v1",        description="Your API Description",        terms_of_service="https://www.example.com/terms/",        contact=openapi.Contact(email="salehzadeh@gmail.com"),        license=openapi.License(name="Your License"),    ),    public=True,    permission_classes=(permissions.AllowAny,),)urlpatterns = [    # ... (other URL patterns)    path('search/', views.search_transactions, name='search_transactions'),    path('transactions/', views.transaction_list, name='transaction_list'),    path('create_transaction/', views.create_transaction, name='create_transaction'),    path('rest_create_transaction/', rest_views.create_transaction, name='create_transaction_service'),    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),         name='schema-swagger-ui'),]
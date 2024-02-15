from django.urls import path
from .views import registration_view,ItemList
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny


schema_view = get_schema_view(
   openapi.Info(
      title="Kaizntree API",
      default_version='v1',
      description="API documentation for Kaizntree",
      terms_of_service="https://www.kaizntree.com/policies/terms/",
      contact=openapi.Contact(email="contact@kaizntree.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(AllowAny,),
)

urlpatterns = [
   path('register/', registration_view, name='api_register'),
   path('login/', obtain_auth_token, name='api_login'),
   path('items/', ItemList.as_view(), name='item-list'),

   # Swagger documentation
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

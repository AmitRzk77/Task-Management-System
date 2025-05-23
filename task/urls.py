"""
URL configuration for task project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from users.routers.routers import router as user_urls
from tasks.routers.tasks_routers import router as tasks_urls
from users.viewsets.users_viewsets import CustomAuthToken

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = routers.DefaultRouter()
router.registry.extend(user_urls.registry)
router.registry.extend(tasks_urls.registry)



schema_view = get_schema_view(
   openapi.Info(
      title="TaskManager API",
      default_version='v1',
      description="Library Backend System",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="prashantkarna21@gmail.com"),
      license=openapi.License(name="No License"),
      **{'x-logo': {'url': 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_120x44dp.png'}},
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('login/', CustomAuthToken.as_view(), name='users-login'),
    
    
    #path('api/', include('tasks.routers.tasks_routers')),
     path('api/api-auth', include('rest_framework.urls')),
     #path('api/', include(user_urls)),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('/api', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

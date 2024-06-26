"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from project.routers import houses_router, additional_services_router

urlpatterns = [
    path('backend/admin/', admin.site.urls),
    path('backend/api-auth/', include('rest_framework.urls')),
    # Строчка выше - группа url'ов необходимая для авторизации в браузерной версии апи.
    # То же самое с SessionAuthentication в настройках проекта
    path('backend/api/v1/houses/', include(houses_router.urls)),
    path('backend/api/v1/additional_services/', include(additional_services_router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
 + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

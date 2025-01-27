"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from drf_spectacular.views import (SpectacularSwaggerView,
                                   SpectacularRedocView,
                                   SpectacularAPIView)
from django.urls import path, include
from django.contrib import admin
from django.conf.urls import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
]

api_urlpatterns = [
    # path("api/", include("order.urls")),
]


swagger_api = [
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
]

media_urlpatterns = static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += media_urlpatterns\
            + api_urlpatterns\
            + swagger_api

if settings.DEBUG:
    urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

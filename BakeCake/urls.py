"""
URL configuration for BakeCake project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from foodcartapp.views import lk_order, index, lk

urlpatterns = ([
    path('admin/', admin.site.urls),
    path('lk_order/', lk_order),
    path('', index, name='index'),
    path('lk/', lk, name='lk')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))

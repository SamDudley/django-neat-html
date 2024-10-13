"""
URL configuration for example project.

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

from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path

from neats.pages.counter import counter_view


def home(request):
    return TemplateResponse(request, "neats.pages.home.main", {})


urlpatterns = [
    path("", home, name="home"),
    path("counter", counter_view, name="counter"),
    path("admin/", admin.site.urls),
]

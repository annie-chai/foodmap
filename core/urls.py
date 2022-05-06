"""core URL Configuration

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
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),
    path('index.html', views.index),
    path('analyze.html', views.analyze),
    path('coming.html', views.coming),
    path('contact.html', views.contact),
    path('single.html', views.single),
    path('community.html', views.community),
    path('login.html', views.login),
    path('communitypage.html', views.communitypage),
    path('communitypage2.html', views.communitypage2),
    path('Userintroduction.html', views.Userintroduction),
    path('consult.html', views.consult),
    path('menu.html', views.menu),
    path('information.html', views.information),
    path('comment.html', views.comment),
    path('consultchatroom.html', views.consultchatroom),
    path('menuadd.html', views.menuadd),
    path('Storeinformation.html', views.Storeinformation),
    path('map.html', views.map)
]

"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, re_path

from home.views import homePage
from createPlayerData.views import createPlayerDataView
from createPlayerProfile.views import createPlayerProfileView
from playerSearch.views import searchView
from playerProfile.views import profileView
from playerPrediction.views import predictionView
from predictionResult.views import predictionResultView

urlpatterns = [
    re_path(r'^$', homePage, name='home'),
    re_path(r'^createPlayerData.*$', createPlayerDataView, name='createPlayerData'),
    re_path(r'^createPlayerProfile.*$', createPlayerProfileView, name='createPlayerProfile'),
    re_path(r'^playerSearch.*$', searchView, name='playerSearch'),
    re_path(r'^playerProfile.*$', profileView, name='playerProfile'),
    re_path(r'^playerPrediction.*$', predictionView, name='playerPrediction'),
    re_path(r'^predictionResult.*$', predictionResultView, name='predictionResult'),
    path('admin/', admin.site.urls)
]

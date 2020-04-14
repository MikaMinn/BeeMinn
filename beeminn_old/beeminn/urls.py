"""beeminn URL Configuration

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

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from hives.forms import CustomAuthForm
from hives import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^adminoo/', admin.site.urls),
    url(r'^hives/', include(('hives.urls', 'hives'), namespace='hives')),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='hives/login.html/', authentication_form=CustomAuthForm,), name="login"),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name="logout"),
    url(r'^register/$', views.register, name='register'),
]

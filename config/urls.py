"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from pybo import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('pybo/', views.index),
    # pybo/로 시작되는 페이지요청은 모두 pybo/urls.py파일에 있는 URL매핑을 참고하여 처리하라는 의미. 
    # 따라서 pybo/로 시작하는 요청은 이제 config/urls.py가 아닌 pybo/urls.py파일을 통해 처리하게된다.
    path('', include('pybo.urls')),
    path('pybo/', include('pybo.urls')),


    path('', views.index, name='index'), # '/'에 해당하는 path

    # Log - in, out -> common app
    path('common/', include('common.urls')),
    
]


"""red_swinger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/users/', include('modules.Users.urls')),  
]

urlpatterns = [
    # Examples:
    # url(r'^$', 'goodreads.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),    
    url(r'^api/v1/users/', include('modules.Users.urls')),     
    #url(r'^api/v1/auth/$', obtain_jwt_token),     
    #url(r'^api/v1/auth/refresh/$', refresh_jwt_token),
    #url(r'^api/v1/auth/verify/$', verify_jwt_token),
    #url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^docs/', include_docs_urls(title="Swinger APP API")),    
]   #+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    
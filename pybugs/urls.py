"""pybugs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
#from rest_framework.authtoken import views
from django.contrib.auth.views import LoginView
from tickets import views
#from rest_framework import routers
#from pybugs.tickets import views

#router = routers.DefaultRouter()
#router.register(r'tickets', views.TicketListAPIView)

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    #url(r'^tickets/api/', include('tickets.urls')),
    #url(r'^$', views.homepage, name="home"),
    path('', include('tickets.urls')),
    path('tickets/api/', include('tickets.urls')),
    #path('update/<int:id>/', views.post_update, name='update'),
    #path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
    #path('login/', LoginView.as_view(template_name="tickets/login.html"), name='Log In'),
    #path('logout/', LoginView.as_view(template_name="tickets/logout.html"), name="Log Out"),
    path('login/', views.account_login, name='Log In'),
    path('logout/', views.account_logout, name='Log Out'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

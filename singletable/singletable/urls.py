"""singletable URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
import userApp.views
import recipeApp.views
import purchaseApp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', userApp.views.main, name='main'),
    path('user/login/', userApp.views.login, name='login'),
    path('user/logout/', userApp.views.logout, name='logout'),
    path('user/signup/', userApp.views.signup, name='signup'),
    path('user/activate/<str:uid64>/<str:token>/', userApp.views.activate, name='activate'),
    path('user/portal_verify/', userApp.views.portal_verify, name='portal_verify'),
    path('user/verification_code/', userApp.views.verification_code, name='verification_code'),
    path('user/new_password/', userApp.views.new_password, name='new_password'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

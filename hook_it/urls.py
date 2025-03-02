"""
URL configuration for hook_it project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# from .views import handler404, handler500, handler400, handler403
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bag/', include('bag.urls')),
    path('pattern/', include('patterns.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('checkout/', include('checkout.urls')),
    path('profiles/', include('profiles.urls')),
    path('contact_us/', include('contact_us.urls')),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    # This includes the patterns app URLs
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handler404 = 'hook_it.views.handler404'
# handler400 = "hook_it.views.handler400"
# handler403 = "hook_it.views.handler403"
# handler500 = "hook_it.views.handler500""""

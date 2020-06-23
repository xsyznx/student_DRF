from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^rest-api/', include('rest_framework.urls')),
    url(r'^user', include('user.urls')),
]



from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('api/auth/signup/', include('accounts.urls')),
    path('api/auth/login/', include('accounts.urls')),
    path('api/auth/register/', include('accounts.urls')),
    path('api/auth/logout/', include('accounts.urls')),
    path('api/auth/password_change/', include('accounts.urls')),

]

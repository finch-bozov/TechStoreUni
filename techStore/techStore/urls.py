from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Web pages
    path('', include('store.web.urls')),

    # Endpoints
    path('api/', include('store.api.urls')),
]
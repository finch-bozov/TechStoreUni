from django.urls import path, include

urlpatterns = [
    path('api/', include('store.api.urls')),
    path('', include('store.web.urls')),
]
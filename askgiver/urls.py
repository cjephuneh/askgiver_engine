# askgiver/urls.py (your project's main URL configuration)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authorization.urls')),
    path('api/products/', include('products.urls')),
    # Add more app-specific URLs as needed
]

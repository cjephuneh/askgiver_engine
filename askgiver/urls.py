# askgiver/urls.py (your project's main URL configuration)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authorization.urls')),
    path('api/products/', include('products.urls')),
    path('api/csrinitiative', include('csrinitiative.urls')),
    path('api/account/', include('useraccount.urls')),

    # Add more app-specific URLs as needed
]

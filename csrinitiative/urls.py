from django.urls import path, include
from rest_framework.routers import DefaultRouter
from csrinitiative.views import CsrInitiativeView

router = DefaultRouter()
router.register(r'csrinitiative', CsrInitiativeView)

urlpatterns = [
    path('', include(router.urls)),
]

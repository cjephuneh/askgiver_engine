from django.urls import path
from .views import SubscriptionView

urlpatterns = [
    path('manage-subscription/', SubscriptionView.as_view(), name='manage-subscription'),
]

from django.urls import path
from .views import AnalyticsSubmitView

urlpatterns = [
    path('submit-analytics/', AnalyticsSubmitView.as_view(), name='submit-analytics'),
]

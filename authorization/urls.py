from django.urls import path
from rest_framework import routers


from .views import UserRegisterView, UserLoginView, ForgotPasswordView

app_name  = 'auth'

router = routers.DefaultRouter()
router.register(r'register', UserRegisterView, 'userregister')
router.register(r'login', UserLoginView, 'userlogin')
router.register(r'forgotpass', ForgotPasswordView, 'forgotpassword')






urlpatterns = router.urls 
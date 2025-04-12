
from django.urls import path
from .views import register_user, logout_user, protected_view, make_request
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    # path("register/", RegisterView.as_view(), name="rest_register"),
    # path("login/", LoginView.as_view(), name="rest_login"),
    # path("logout/", LogoutView.as_view(), name="rest_logout"),
    # path("user/", UserDetailsView.as_view(), name="rest_user_details"),
    path('api/register/', register_user, name='register_user'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/logout/', logout_user, name='logout_user'),
    path('api/protected/', protected_view, name='protected_view'),
    path('api/make_request/', make_request, name='make_request'),
]
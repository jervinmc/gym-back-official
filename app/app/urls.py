from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.urls.conf import include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from users.views import Login,GetUserView,Signup,GetUser
from transaction.views import TransactionNotif,TransactionAllByUser
from book.views import CheckBook
from attendance.views import AttendanceView
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
path('api/v1/admin/', admin.site.urls),
    path('api/v1/signup/', Signup.as_view(), name='Sign up'),
    path('api/v1/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/transaction-user/', TransactionAllByUser.as_view(), name='token_refresh'),
    path('api/v1/auth/user/', GetUserView.as_view(), name='auth_data'),
    path('api/v1/login/', Login.as_view(), name='token_refresh'),
    path('api/v1/check-book/', CheckBook.as_view(), name='token_refresh'),
    path('api/v1/get-user/', GetUser.as_view(), name='token_refresh'),
    path('api/v1/transaction-notif/', TransactionNotif.as_view(), name='token_refresh'),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/transaction/', include('transaction.urls')),
    path('api/v1/attendance/', include('attendance.urls')),
    path('api/v1/book/', include('book.urls')),
    path('api/v1/product/', include('product.urls')),
    path('api/v1/exercise/', include('exercise.urls')),
    # path('api/v1/users/details/', GetUserView.as_view(), name='get_user'),
]
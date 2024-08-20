from users.apps import UsersConfig
from django.urls import path

from users.views import UserListApiView, UserUpdateApiView, UserCreateApiView, UserDeleteApiView, PaymentsListApiView, \
    PaymentsCreateApiView

app_name = UsersConfig.name

urlpatterns = [
    path('', UserListApiView.as_view(),name='users_list'),
    path('update/<int:pk>', UserUpdateApiView.as_view(), name='user_update'),
    path('create/', UserCreateApiView.as_view(), name='user_create'),
    path('delete/<int:pk>', UserDeleteApiView.as_view(),name='user_delete'),
    path('payments/', PaymentsListApiView.as_view(), name='payments_list'),
    path('payments_pay/', PaymentsCreateApiView.as_view(), name='payments_pay'),
]



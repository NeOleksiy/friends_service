from django.urls import path
from friend_api.views import InviteApiView, RegistrationApiView, FriendListApiView, \
    FriendStatusApiView, AcceptRejectApiView

urlpatterns = [
    path('invite_or_delete/<int:pk_user1>/<int:pk_user2>/', InviteApiView.as_view(), name='invite_or_delete'),
    path('accept_or_reject/<int:pk_user1>/<int:pk_user2>/', AcceptRejectApiView.as_view(), name='accept_or_reject'),
    path('register/', RegistrationApiView.as_view(), name='register'),
    path('friend_list/<int:pk_user>', FriendListApiView.as_view(), name='friend_list'),
    path('friend_status/<int:pk_user1>/<int:pk_user2>', FriendStatusApiView.as_view(), name='friend_status'),
]

"""
URL configuration for friends_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from friend_api.views import InviteApiView, RegistrationApiView, FriendListApiView, FriendStatusApiView, AcceptRejectApiView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/invite_or_delete/<int:pk_user1>/<int:pk_user2>/', InviteApiView.as_view(), name='invite_or_delete'),
    path('api/accept_or_reject/<int:pk_user1>/<int:pk_user2>/', AcceptRejectApiView.as_view(), name='accept_or_reject'),
    path('api/register/', RegistrationApiView.as_view(), name='register'),
    path('api/friend_list/<int:pk_user>', FriendListApiView.as_view(), name='friend_list'),
    path('api/friend_status/<int:pk_user1>/<int:pk_user2>', FriendStatusApiView.as_view(), name='friend_status'),
]

from django.urls import path
from user_mgmt.views import UserLoginView, UserLoginOutView

urlpatterns = [
   path('login',UserLoginView.as_view(),name="UserLogin"),
   path('logout',UserLoginOutView.as_view(),name="UserLogOut"),
]

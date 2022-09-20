from django.contrib.auth.views import LogoutView
from django.urls import path

from apps.common.views import HomePageView, LoginPageView

app_name = 'common'


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

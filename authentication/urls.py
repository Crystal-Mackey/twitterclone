from django.urls import path
from authentication import views as v

urlpatterns = [
    path('login/', v.login_view, name='loginview'),
    path('logout/', v.logout_view, name='logoutview'),
    path('register/', v.register_view, name='registerview'),
]
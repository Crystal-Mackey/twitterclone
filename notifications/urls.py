from django.urls import path
from notifications import views
urlpatterns = [
    path('notifications/', views.notification_view, name="notifications"),
]
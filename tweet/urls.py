from django.urls import path
from tweet import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('home/', views.homepage, name='homepage'),
    path('create/', views.create_tweet, name='createtweet'),
    path('tweet/<int:tweet_id>/', views.tweet_detail, name='tweetdetail'),
    path('follow/<str:username>/', views.follow_view, name='follow'),
    path('unfollow/<str:username>/', views.unfollow_view, name='unfollow'),
    path('profile/<str:username>/', views.profile_detail, name='userprofile'),
]
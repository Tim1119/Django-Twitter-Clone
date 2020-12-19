from django.urls import path,include
from .views import HomeView,DeletePostView,EditPostView,CommentView,LikeView,CreateTweetView,EditProfileView,CreateProfileView,ShowProfileView,FollowView,DisplaySearchedUserView,LikeSearchedUserView
urlpatterns = [
    path('',HomeView,name='home'),
    path('delete/<int:id>',DeletePostView,name='delete-post'),
    path('edit/<int:id>',EditPostView,name='edit-post'),
    path('comment/<int:id>',CommentView,name='comment'),
    path('like/<int:pk>',LikeView,name='like_post'),
    path('create-tweet/',CreateTweetView,name='create-tweet'),
    path('edit_profile/<int:pk>',EditProfileView,name='edit_profile'),
    path('create_profile/',CreateProfileView,name='create_profile'),
    path('show_profile/<int:pk>',ShowProfileView,name='show_profile'),
    path('follow/<int:pk>',FollowView,name='follow'),
    path('view-user/<int:pk>',DisplaySearchedUserView,name='view-user'),
     path('user-search-like/<int:pk>',LikeSearchedUserView,name='like_user_post'),
]

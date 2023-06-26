from django.urls import include, path,re_path
from .views.login import Custom_AuthToken
from .views.register import UserRegistrationView
from .views.profile.edit_profile import ProfileUpdateView
from .views.profile.display_profile import ProfileDetailView
from .views.profile.create_profile import CreateProfileView
from .views.profile.profile_list import ProfileView

from .views.posts.create_posts import PostCreateView
from .views.posts.post_list import PostListView
from .views.posts.posts_actions import PostDetailView, PostLikeView, PostCommentView, PostShareView



from .views.connection.connect_users import ConnectionView, FeedView
from .views.connection.connection_manager import UserConnectionListView, ConnectionCreateView, ConnectionDetailView



urlpatterns = [
    ### Profile ###
    ## Authentication [Login/Gain Token]
    path('login/', Custom_AuthToken.as_view(), name='Login'),
    # Register User
    path('register/', UserRegistrationView.as_view(), name='register'),
    # Create Profile
    path('create-profile/', CreateProfileView.as_view(), name='create-profile'),
    # Update/Edit Profile
    path('profile/self/', ProfileDetailView.as_view(), name='display-profile'),
    # Update/Edit Profile
    path('profile/update/', ProfileUpdateView.as_view(), name='update-profile'),
    # List of Profiles
    path('profiles/', ProfileView.as_view(), name='profile-detail'),

    
    
    ### Posts ###
    # Create Posts
    path('posts/create/', PostCreateView.as_view(), name='post-create'),
    # Create Posts
    path('posts/', PostListView.as_view(), name='post-list'),
    ## posts action
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/like/', PostLikeView.as_view(), name='post-like'),
    path('posts/<int:pk>/comment/', PostCommentView.as_view(), name='post-comment'),
    path('posts/<int:pk>/share/', PostShareView.as_view(), name='post-share'),

    ## Connect Users and Get Feeds
    path('connections/', ConnectionView.as_view(), name='connect-users'),
    path('feed/', FeedView.as_view(), name='feed'),

    ## Connections Manager
    path('connections-list/', UserConnectionListView.as_view(), name='connection-list'),
    path('connections/create/', ConnectionCreateView.as_view(), name='connection-create'),
    path('connections/<int:pk>/', ConnectionDetailView.as_view(), name='connection-detail'),


]
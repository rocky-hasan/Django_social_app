from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('settings/', views.SettingsView.as_view(), name="settings"),
    path('upload/', views.UploadView.as_view(), name="upload"),
    path('follow/', views.FollowView.as_view(), name="follow"),
    path('search/', views.SearchView.as_view(), name="search"),
    path('profile/<str:pk>/', views.ProfileView.as_view(), name="profile"),
    path('like/', views.LikePostView.as_view(), name="like"),
    path('signup/', views.SignupView.as_view(), name="signup"),
    path('signin/', views.SigninView.as_view(), name="signin"),
    path('logout/',views.LogoutView.as_view() ,name="logout")
]
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from login import views as login_views

urlpatterns = [
    path('', include('MMORPG.urls')),
    path('admin/', admin.site.urls),
    path('register/', login_views.register, name='register'),
    path('profile/', login_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('pages/', include('django.contrib.flatpages.urls')),
]

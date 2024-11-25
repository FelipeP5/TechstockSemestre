from django.urls import path
from .views import LoginView, LogoutView, ProfileView, EditProfileView

urlpatterns = [
    path('', LoginView.as_view(), name= 'login'),
    path('login/logout/', LogoutView.as_view(), name= 'logout'),
    path('login/perfil/', ProfileView.as_view(), name= 'perfil'),
    path('login/editarperfil', EditProfileView.as_view(), name= 'editar_perfil'),
]

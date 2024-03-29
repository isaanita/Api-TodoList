from django.contrib import admin
from LoginAndRegister.views import RegisterAPI, PasswordTokenCheckAPI
from django.urls import path, include
from knox import views as knox_view
from LoginAndRegister.login_views import LoginAPI
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.contrib.auth import views as auth_views
from LoginAndRegister.changepass_views import ChangePasswordView


schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),

    # Swagger URL
    path('Swagger', schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),

    # Register, login and logout URL for user
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_view.LogoutView.as_view(), name='logout'),
    path('logout-all/', knox_view.LogoutAllView.as_view(), name='logout-all'),

    # todolist URL
    path('todolist/', include('Todos.urls')),


    #reset password urls
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

    # change password URL
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),

    path('password-reset/<uidb64>/token/', PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    

]


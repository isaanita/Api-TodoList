from django.contrib import admin
from django.urls import path
from LoginAndRegister.views import RegisterAPI
from django.urls import path, include
from knox import views as knox_view
from LoginAndRegister.login_views import LoginAPI
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

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
    path('logoutall/', knox_view.LogoutAllView.as_view(), name='logoutall'),

    # todolist URL
    path('todolist/', include('Todos.urls')),

]


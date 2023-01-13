from django.conf.urls.static import static
from django.urls import path

from django_blogm import settings
from .views import index, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name='index'),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('register/', RegisterPage.as_view(), name="register"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
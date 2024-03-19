from django import views
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from django.conf import settings
from django.conf.urls.static import static
from .views import GetImages, Products

urlpatterns = [
    path('login', TokenObtainPairView.as_view()),  # Added trailing slash
    path('images/', GetImages.as_view(), name='get-images'),
    path('products/', Products),  # Added trailing slash
    path('products/<int:id>/', Products),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
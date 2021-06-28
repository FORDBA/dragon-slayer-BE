from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings


"""Router"""
router = routers.DefaultRouter(trailing_slash=False)




urlpatterns = [
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

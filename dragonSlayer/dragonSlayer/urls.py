from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from dragonslayerapi.views import register_user, login_user, DungeonViewSet, PlayerClassViewSet, BossStatusViewSet, ProfessionViewSet
from dragonslayerapi.views import RaceViewSet, RankViewSet, RoleViewSet
from django.conf.urls.static import static
from django.conf import settings


"""Router"""
router = routers.DefaultRouter(trailing_slash=False)
router.register(r'dungeons', DungeonViewSet, 'dungeon')
router.register(r'playerclasses', PlayerClassViewSet, 'playerclass')
router.register(r'bossstatuses', BossStatusViewSet, 'bossstatus')
router.register(r'professions', ProfessionViewSet, 'profession')
router.register(r'races', RaceViewSet, 'race')
router.register(r'ranks', RankViewSet, 'rank')
router.register(r'roles', RoleViewSet, 'role')

urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

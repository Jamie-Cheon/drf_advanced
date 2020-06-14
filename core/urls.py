from rest_framework import routers
from .views import UserViewSet, CardViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'users', UserViewSet)
router.register(r'users/<int:pk>', UserViewSet)
router.register(r'cards', CardViewSet)
router.register(r'cards/<int:pk>', CardViewSet)
urlpatterns = router.urls


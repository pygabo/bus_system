from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from bus_system.apps.bus.views import BusViewSet
from bus_system.apps.bus_driver.views import BusDriverViewSet
from bus_system.apps.passenger.views import PassengerViewSet
from bus_system.apps.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet, basename='users')
router.register("bus", BusViewSet, basename='bus')
router.register("driver", BusDriverViewSet, basename='driver')
router.register("passenger", PassengerViewSet, basename='passenger')

app_name = "api"
urlpatterns = router.urls

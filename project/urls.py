from rest_framework import routers
from .api import ArticuloViewSet

router = routers.DefaultRouter()

router.register('api/project', ArticuloViewSet, 'articulos')

urlpatterns = router.urls

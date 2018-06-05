from django.conf.urls import url, include
from rest_framework import routers

from europolapi import views

routerv1 = routers.DefaultRouter()
routerv1.register(r'vehicles', views.V1VehicleViewset)

router = routers.DefaultRouter()
router.register(r'vehicles', views.VehicleViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(routerv1.urls)),
    url(r'^v2/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
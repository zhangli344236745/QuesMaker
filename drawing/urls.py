from django.urls import path
from rest_framework.routers import DefaultRouter
from drawing.views import SensorViewSet,ProjectViewSet,DataViewSet,DrawingViewSet

router = DefaultRouter()

router.register('sensors',SensorViewSet,basename="sensors")
router.register('projects', ProjectViewSet, basename='projects')
router.register('datas', DataViewSet, basename='datas')
router.register('drawings', DrawingViewSet, basename='drawings')

urlpatterns = [
]

urlpatterns += router.urls

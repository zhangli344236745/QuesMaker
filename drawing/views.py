from rest_framework.viewsets import ModelViewSet
from drawing.models import Sensor,Project,Data,Drawing
from drawing.serializer import SensorSerializer,ProjectSerializer,DataSerializer,DrawingSerializer
from drawing.filter import SensorFitler,ProjectFilter,DrawingFilter,DataFilter
from django_filters.rest_framework import DjangoFilterBackend

class SensorViewSet(ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = SensorFitler

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = ProjectFilter

class DataViewSet(ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = DrawingFilter


class DrawingViewSet(ModelViewSet):
    queryset = Drawing.objects.all()
    serializer_class = DrawingSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = DrawingFilter
    search_fields = ('drawing_name', 'material_code', 'drawing_spec', 'drawing_client_id')



from django_filters import FilterSet,filters
from drawing.models import *

class SensorFitler(FilterSet):
    sensor_name = filters.CharFilter(field_name='sensor_name', lookup_expr="icontains")
    class Meta:
        model = Sensor
        fields = ('sensor_name',)


class ProjectFilter(FilterSet):
    class Meta:
        model = Project
        fields = ('project_name','sensor')

# ---Data的Filter类---
class DataFilter(FilterSet):
    class Meta:
        model = Data
        fields = ('data_name', 'sensor', 'project')

class DrawingFilter(FilterSet):
    class Meta:
        model = Drawing
        fields = ('drawing_name', 'material_code', 'drawing_spec', 'drawing_client_id')






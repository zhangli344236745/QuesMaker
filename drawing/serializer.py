from drawing.models import *
from rest_framework import serializers


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('id',"sensor_name",)
        #fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    sensor = SensorSerializer()
    sensor_id = serializers.IntegerField(source="sensor.id",read_only=True)
    sensor_name = serializers.CharField(source="sensor.sensor_name",read_only=True)
    class Meta:
        model = Project
        fields = "__all__"


class DataSerializer(serializers.ModelSerializer):
    sensor = SensorSerializer()
    sensor_name = serializers.CharField(source='sensor.sensor_name',read_only=True)
    class Meta:
        model = Data
        fields = "__all__"


class DrawingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drawing
        fields = "__all__"


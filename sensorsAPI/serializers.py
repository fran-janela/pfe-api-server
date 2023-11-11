from rest_framework import serializers
from sensorsAPI.models import SensorMeasure

class SensorMeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorMeasure
        fields = ('id', 
                  'sensor_id', 
                  'temperature', 
                  'temperature_unit', 
                  'humidity', 
                  'humidity_unit', 
                  'pressure', 
                  'pressure_unit', 
                  'voltage', 
                  'voltage_unit', 
                  'current', 
                  'current_unit', 
                  'power', 
                  'power_unit', 
                  'internet_ping', 
                  'internet_ping_unit', 
                  'internet_speed', 
                  'internet_speed_unit')

        """
        "sensor_id": 1, 
        "temperature": 23.0, 
        "temperature_unit": "C", 
        "humidity": 44.51, 
        "humidity_unit": "%", 
        "pressure": 927.87, 
        "pressure_unit": "hPa", 
        "voltage": 0.896
        "voltage_unit": "V", 
        "current": -0.09756097, 
        "current_unit": "mA", 
        "power": 0.0, 
        "power_unit": "mW", 
        "internet_ping": 4.238, 
        "internet_ping_unit": "s", 
        "internet_speed": 12.56442, 
        "internet_speed_unit": "KB/s", 
        """
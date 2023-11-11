from django.db import models
from datetime import datetime

# Create your models here.
class SensorMeasure(models.Model):
    sensor_id = models.IntegerField()
    temperature = models.FloatField()
    temperature_unit = models.CharField(max_length=1)
    humidity = models.FloatField()
    humidity_unit = models.CharField(max_length=1)
    pressure = models.FloatField()
    pressure_unit = models.CharField(max_length=3)
    voltage = models.FloatField()
    voltage_unit = models.CharField(max_length=1)
    current = models.FloatField()
    current_unit = models.CharField(max_length=2)
    power = models.FloatField()
    power_unit = models.CharField(max_length=2)
    internet_ping = models.FloatField()
    internet_ping_unit = models.CharField(max_length=100)
    internet_speed = models.FloatField()
    internet_speed_unit = models.CharField(max_length=100)
    timestamp = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return str(self.sensor_id) + " - " + str(self.time)
    

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
from django.shortcuts import render
from rest_framework.views import APIView
from sensorsAPI.models import SensorMeasure
from sensorsAPI.serializers import SensorMeasureSerializer
from rest_framework import status
from rest_framework.response import Response
import json


class TestConectionTimeView(APIView):
    '''
    Class responsible for testing the connection time between the server and the client.
    '''
    def get(self, request, format=None):
        return Response({"message": "Test Conection Time"})

class SensorMeasureListView(APIView):
    '''
    Class responsible for realizing the POST request for the sensor measures.
    '''
    def post(self, request, format=None):
        measure_data = json.loads(request.data)
        print("received data:")
        print(measure_data)
        serializer = SensorMeasureSerializer(data=measure_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
from django.urls import path
from django.conf.urls import include

from .views import SensorMeasureListView

urlpatterns = [
    path("measure/", SensorMeasureListView.as_view()),
]
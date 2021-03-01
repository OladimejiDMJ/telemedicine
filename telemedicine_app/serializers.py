from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Appointment,BlockedTime
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','email','role')


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Appointment
        fields=['username','time_start','time_end','room_number','appointment_with','date']


class BlockedTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model=BlockedTime
        fields=['username','date','start_time','end_time']

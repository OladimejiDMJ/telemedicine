from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser
from .models import Appointment, BlockedTime
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, AppointmentSerializer, BlockedTimeSerializer
from django.contrib.auth.models import User, Group



@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def create_blockedtime(request):
    blockedtime_data=JSONParser().parse(request)
    group=Group.objects.all().filter(user=request.user)
    group=str(group[0])
    blockedtime_data["username"]=request.user.get_username()
    bt_serializer=BlockedTimeSerializer(data=blockedtime_data)
    if "Patients"==group:
        return HttpResponse("You are not to create blocked time as a patient. You are only allowed to create appointment")
    else:
        pass
    if bt_serializer.is_valid():
        bt_serializer.save()
        return JsonResponse(bt_serializer.data)
    return JsonResponse(bt_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    



@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def my_appointment(request):
    username=request.user.get_username()
    appointments=Appointment.objects.all().filter(username=username)
    appointment_serializer=AppointmentSerializer(appointments,many=True)
    print(request.user.id)
    print(appointment_serializer.data)
    return JsonResponse(appointment_serializer.data,safe=False)


@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def create_appointment(request):
    appointment_data=JSONParser().parse(request)
    group=Group.objects.all().filter(user=request.user)
    group=str(group[0])
    appointment_data['username']=request.user.get_username()
    appointment_serializer=AppointmentSerializer(data=appointment_data)
    #blocked_time=BlockedTime.objects.all()
    if "Doctors"==group:
        print(group)
        return HttpResponse("You are not allowed to create appointment as a doctor")
    else:
        group='Patients'
    if appointment_serializer.is_valid():
        doctor_unavailable=BlockedTime.objects.filter(username=appointment_serializer.validated_data['appointment_with'],start_time=appointment_serializer.validated_data['time_start'],date=appointment_serializer.validated_data['date']).all()
    if doctor_unavailable:
        return HttpResponse(appointment_serializer.initial_data['appointment_with'] +' ' + 'has an appointment at this time. You have to book appointment for another time')
    else:
        appointment_serializer.save()
        return JsonResponse(appointment_serializer.data)
    return JsonResponse(appointment_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def my_calender(request):  
    username=request.user.get_username()
    calender=BlockedTime.objects.all().filter(username=username)
    calender_serializer=BlockedTimeSerializer(calender,many=True)
    return JsonResponse(calender_serializer.data,safe=False)
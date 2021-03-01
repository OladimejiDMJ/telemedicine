from django.db import models
from django.contrib.auth.models import User, Group, AbstractUser
from django.conf import settings
from django.dispatch import receiver
from djoser.signals import user_registered



# Database creation for Doctor`s appointment.

class User(AbstractUser):
    DOCTOR='Dr'
    PATIENT='Pt'
    role_choices=[(DOCTOR,'Doctor'),(PATIENT,'Patient')]
    role=models.CharField(max_length=15,choices=role_choices)
    REQUIRED_FIELDS=["email","role"]

    def set_group(self):
        user=User.objects.get(username=self.username)
        if self.role==self.DOCTOR:
            group=Group.objects.get(name="Doctors")
            user.groups.add(group)
            #group.user_set.add(user)
        if self.role==self.PATIENT:
            group=Group.objects.get(name="Patients")
            user.groups.add(group)
            #group.user_set.add(user)
            
    # def create_user(self,username,*args,**kwargs):
    #     user=super().create_user(username=username,*args,**kwargs)
    #     user.save()
    #     print(user)
    #     self.set_group()
    #     return user

@receiver(user_registered)
def my_handler(user,request,*args,**kwargs):
    # print(user)
    # print(dir(user))
    user.set_group()
    user.save()
   
class Appointment(models.Model):

    #user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING)
    username=models.CharField(max_length=50)
    date=models.DateField()
    time_start=models.TimeField()
    appointment_with=models.CharField(max_length=50)
    time_end=models.TimeField()
    room_number=models.CharField(max_length=50)
    update_time=models.DateField(auto_now=True, auto_now_add=False)
    
    
    def __str__(self):
        user=str(self.username)
        return "%s %s %s %s" %(user,self.date,self.appointment_with,self.time_end)


class BlockedTime(models.Model):
    
    username=models.CharField(max_length=50)
    date=models.DateField()
    start_time=models.TimeField()
    end_time=models.TimeField()
    def __str__(self):
        user=str(self.username)
        return "%s %s " %(self.date,self.start_time)







# Create your models here.

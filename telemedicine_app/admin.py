from django.contrib import admin
from .models import Appointment, BlockedTime, User
#admin.site.register(Appointment)
# admin.site.register(BlockedTime)
# admin.site.register(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=("role","username")
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display=("username","appointment_with","time_start","time_end","date","room_number","update_time")
@admin.register(BlockedTime)
class BlockedTimeAdmin(admin.ModelAdmin):
    list_display=("username","date","start_time","end_time")
# Register your models here.

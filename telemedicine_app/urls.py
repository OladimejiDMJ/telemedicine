from django.conf.urls import url, include
from . import views
from .views import create_appointment,my_appointment

urlpatterns=[
    url(r'^api/v1/', include('djoser.urls')),
    url(r'^api/v1/', include('djoser.urls.authtoken')),
    url(r'^create_appointment/',views.create_appointment),
    url(r'^my_appointment/',views.my_appointment),
    url(r'^create_blockedtime/',views.create_blockedtime),
    url(r'^my_calender/',views.my_calender),
]
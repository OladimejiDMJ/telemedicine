# telemedicine
An API developed with the Django framework where patient can book appointment with doctors at appropriate times and doctors can block off unavailable date.
#Enpoints
Before anything try creating a superuser for the admin. Log into the admin and navigate to groups to create two groups (Doctors and Patients). After this then you can continue with the endpoints.
1) Signup-/api/v1/users
2) Login-/api/v1/token/login
3) Create appointment-/create_appointment
4) View my appointment-/my_appointment/
5) View my calendar-/my_calender
6) Create blocked time-/create_blockedtime

A doctor is not allowed to create appointment and a patient is not allowed to create blocked time.

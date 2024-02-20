from django.urls import path

from .views import home,personal_info,timesheet_submit

urlpatterns = [
    path('home',home,name='home'),
    path('personal_info',personal_info,name='personal_info'),
    path('timesheet_submit',timesheet_submit,name='timesheet_submit'),
]

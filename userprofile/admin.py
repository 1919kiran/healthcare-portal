from django.contrib import admin
from userprofile.models import DoctorModel, PatientModel

# Register your models here.
admin.site.register(DoctorModel)
admin.site.register(PatientModel)

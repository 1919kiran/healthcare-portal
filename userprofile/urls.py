from django.urls import path
from . import views

app_name='userprofile'

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/signup_option/', views.signup_option, name='signup_option'),
    path('select_patient', views.select_patient, name='select_patient'),
    path('diagnose_patient', views.diagnose_patient, name='diagnose_patient'),
]

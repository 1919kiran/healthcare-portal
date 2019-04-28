from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from allauth.socialaccount.models import SocialAccount
from django.db import models
from django.contrib.auth.models import User
from userprofile.forms import DoctorForm, PatientForm, SignupOptionForm, PatientDiagnoseForm
from userprofile.models import DoctorModel, PatientModel

# Create your views here.

def index(request):
    return render(request, 'index.html', None)

def about(request):
    return render(request, 'about.html', None)

def signup_option(request):
    #signup as patient, doctor or pharmacist
    if request.method == 'POST':
        form = SignupOptionForm(request.POST)
        if form.is_valid():
            request.session['category'] = form.cleaned_data.get('category')
            return redirect('userprofile:signup')
    else:
        form = SignupOptionForm()

    return render(request, 'signup_option.html', {'form': form})


def signup(request):
    #setting form as patientform by default
    form = PatientForm(request.POST)
    category = ''
    if 'category' in request.session:
        category = request.session['category']
    else:
        return HttpResponse('<h1>Already registered....</h1>')

    if request.method == 'POST':
        #assign form type for post request
        if category == 'Patient':
            form = PatientForm(request.POST)
        elif category == 'Doctor':
            form = DoctorForm(request.POST)

        if form.is_valid():
            #signup based on category
            social_accounts = SocialAccount.objects.all()
            if category == 'Patient':
                patient = form.save(commit=False)
                patient.user = request.user
                patient.user_social = social_accounts.get(user=request.user)
                patient.save()
                return redirect('userprofile:profile')
            elif category == 'Doctor':
                doctor = form.save(commit=False)
                doctor.user = request.user
                doctor.user_social = social_accounts.get(user=request.user)
                doctor.save()
                return redirect('userprofile:profile')
            else:
                return HttpResponse('<h1>Not appropriate category</h1>')
    else:
        print(category)
        if category == 'Patient':
            form = PatientForm()
        elif category == 'Doctor':
            form = DoctorForm()

    return render(request, 'signup.html', {'form': form})


def profile(request):
    #fetching all objects
    patient_accounts = PatientModel.objects.all()
    doctor_accounts = DoctorModel.objects.all()

    #checking if logged in user is registered in DoctorModel and PatientModel
    #variables are true if user is found in these models
    is_patient = is_doctor = False

    if patient_accounts.filter(email=request.user.email).exists():
        is_patient = patient_accounts.filter(email=request.user.email).exists()
        patient_account = patient_accounts.get(pk=request.user.email)
    elif doctor_accounts.filter(email=request.user.email).exists():
        is_doctor = doctor_accounts.filter(email=request.user.email).exists()
        doctor_account = doctor_accounts.get(pk=request.user.email)

    if is_doctor==False and is_patient==False:
        #enforce user registration
        return redirect('userprofile:signup_option')

    else:
        if is_patient:
            return render(request, 'profile_patient.html', {'patient_account': patient_account})

        elif is_doctor:
            patients_diagnosed = patient_accounts.filter(diagnosed_by=doctor_account)
            print(patients_diagnosed)

            return render(request, 'profile_doctor.html', {'doctor_account': doctor_account, 'patients_diagnosed': patients_diagnosed})

    return render(request, 'profile.html', None)


def select_patient(request):
    #selects from a list of patients
    if request.method == 'POST':
        request.session['patient_email'] = request.POST['patient_email']
        patient_accounts = PatientModel.objects.all()
        patient = get_object_or_404(PatientModel, email=request.POST['patient_email'])

        form = PatientDiagnoseForm(request.POST, instance=patient)
        return redirect('userprofile:diagnose_patient')

    patient_accounts = PatientModel.objects.all()
    available_patients = patient_accounts.filter(is_open_for_appointment=True)
    return render(request, 'select_patient.html', {'available_patients': available_patients})



def diagnose_patient(request):
    #gives a form to doctor to edit patient details
    patient = get_object_or_404(PatientModel, email=request.session['patient_email'])
    form = PatientDiagnoseForm(instance=patient)

    if request.method == 'POST':
        form = PatientDiagnoseForm(request.POST, instance=patient)
        print(form.errors)
        if form.is_valid():
            patient = form.save(commit=False)
            current_doctor = get_object_or_404(DoctorModel, user=request.user)
            patient.diagnosed_by = current_doctor
            patient.save()
            return redirect('userprofile:profile')
        return render(request, 'edit_patient_details.html', {'form': form})

    else:
        print(form.errors)
        form = PatientDiagnoseForm(instance=patient)
    return render(request, 'edit_patient_details.html', {'form': form})


def view_profile_patient(request):
    #views the patient form
    patient = get_object_or_404(PatientModel, email=request.user.email)
    form = PatientForm(instance=patient)
    return render(request, 'view_profile.html', {'form': form})

def view_profile_doctor(request):
    #views the patient form
    doctor = get_object_or_404(Doctor, email=request.user.email)
    form = DoctorForm(instance=doctor)
    return render(request, 'view_profile.html', {'form': form})
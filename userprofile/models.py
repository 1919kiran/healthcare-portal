from django.db import models
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount
from multiselectfield import MultiSelectField

# Create your models here.

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)
ILLNESS_CHOICES = (
    ('anemia', 'Anemia'),
    ('asthma', 'Asthma'),
    ('arthiritis', 'Arthritis'),
    ('cancer', 'Cancer'),
    ('gout', 'Gout'),
    ('diabetes', 'Diabetes'),
    ('emotional_disorder', 'Emotional Disorder'),
    ('epilepsy_seizures', 'Epilepsy Seizures'),
    ('fainting_spells', 'Fainting Spells'),
    ('gallstones', 'Gallstones'),
    ('heart_disease', 'Heart Disease'),
    ('heart_attack', 'Heart Attack'),
    ('rheumatic_fever', 'Rheumatic Fever'),
    ('high_blood_pressure', 'High Blood Pressure'),
    ('digestive_problems', 'Digestive Problems'),
    ('ulcerative_colitis', 'Ulcerative Colitis'),
    ('ulcer_disease', 'Ulcer Disease'),
    ('hepatitis', 'Hepatitis'),
    ('kidney_disease', 'Kidney Disease'),
    ('liver_disease', 'Liver Disease'),
    ('sleep_apnea', 'Sleep Apnea'),
    ('use_a_c_pap_machine', 'Use a C-PAP machine'),
    ('thyroid_problems', 'Thyroid Problems'),
    ('tuberculosis', 'Tuberculosis'),
    ('venereal_disease', 'Venereal Disease'),
    ('neurological_disorders', 'Neurological Disorders'),
    ('bleeding_disorders', 'Bleeding Disorders'),
    ('lung_disease', 'Lung Disease'),
    ('emphysema', 'Emphysema'),
)
DOCTOR_QUALIFICATIONS = (
    ('MD', 'MD'),
    ('MS', 'MS'),
    ('MBBS', 'MBBS'),
    ('BDS', 'BDS'),
    ('Other', 'Other'),
)
DOCTOR_DESIGNATION = (
    ('Neurologist', 'Neurologist'),
    ('Pediatrician', 'Pediatrician'),
    ('Psychiatrist', 'Psychiatrist'),
    ('Surgeon', 'Surgeon'),
    ('Veterinarian', 'Veterinarian'),
    ('Homeopathic Doctor', 'Homeopathic Doctor'),
    ('Physiotherapist', 'Physiotherapist'),
    ('Dermatologist', 'Dermatologist'),
    ('Cardiologist', 'Cardiologist'),
    ('Gynecologist', 'Gynecologist'),
    ('Other', 'Other'),
)

class DoctorModel(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    user_social = models.OneToOneField(SocialAccount, null=True, blank=True, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100, primary_key=True)
    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    address = models.CharField(max_length=1000)
    qualification = models.CharField(max_length=100, choices=DOCTOR_QUALIFICATIONS)
    designation = models.CharField(max_length=100, choices=DOCTOR_DESIGNATION)
    registration_number = models.CharField(max_length=100)
    is_approved_by_admin = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)

class PatientModel(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    user_social = models.OneToOneField(SocialAccount, null=True, blank=True, on_delete=models.CASCADE)
    diagnosed_by = models.ForeignKey(DoctorModel, null=True, blank=True, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100, primary_key=True)
    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    age = models.CharField(max_length=3)
    address = models.CharField(max_length=1000)
    height = models.CharField(max_length=4)
    weight = models.CharField(max_length=4)
    reason = models.TextField(max_length=1000)
    prescribed_tablets = models.TextField(max_length=1000, null=True, blank=True)
    drug_allergies = models.TextField(max_length=1000, null=True, blank=True)
    illnesses = MultiSelectField(choices=ILLNESS_CHOICES, max_choices=10, max_length=4000)
    other_illnesses = models.TextField(max_length=1000, null=True, blank=True)
    operations = models.TextField(max_length=1000, null=True, blank=True)
    current_medications = models.TextField(max_length=1000, null=True, blank=True)
    is_open_for_appointment = models.BooleanField(default=True)

    def __str__(self):
        return str(self.user)

from django.forms import ModelForm
from django import forms
from userprofile.models import DoctorModel, PatientModel

class DoctorForm(ModelForm):
    class Meta:
        model = DoctorModel
        fields = '__all__'
        widgets = {
            'email': forms.TextInput(attrs={'readonly':'readonly',
                                            'id': "email"}),
        }
        exclude = ['user', 'user_social',  'is_approved_by_admin']

class PatientForm(ModelForm):
    class Meta:
        model = PatientModel
        fields = '__all__'
        widgets = {
            'email': forms.TextInput(attrs={'readonly':'readonly',
                                            'id': "email"}),
            'height': forms.TextInput(attrs={'class': "form-textbox",
                                             'style': "width:100px",
                                             'placeholder': "ex: 176",
                                             'id': "height"}),
            'weight': forms.TextInput(attrs={'class': "form-textbox",
                                             'style': "width:100px",
                                             'placeholder': "ex: 70",
                                             'id': "weight"}),
        }
        exclude = ['user', 'user_social', 'diagnosed_by']

class SignupOptionForm(forms.Form):
    CHOICES = (
        ('Doctor', 'Doctor'),
        ('Patient', 'Patient'),
        ('Pharmacist', 'Pharmacist'),
    )
    category = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

class PatientDiagnoseForm(PatientForm):
    class Meta:
        model = PatientModel
        fields = '__all__'
        exclude = [
            'user',
            'user_social',
            'diagnosed_by',
            'address',
            'is_open_for_appointment',
        ]
        widgets = {
            'email': forms.TextInput(attrs={'readonly':'readonly',
                                            'id': "email"}),
            'phone': forms.TextInput(attrs={'readonly':'readonly',
                                            'id': "phone"}),
            'gender': forms.TextInput(attrs={'readonly':'readonly',
                                            'id': "gender"}),
            'age': forms.TextInput(attrs={'readonly':'readonly',
                                            'id': "age"}),
            'height': forms.TextInput(attrs={'class': "form-textbox",
                                             'style': "width:100px",
                                             'placeholder': "ex: 176",
                                             'readonly':'readonly',
                                             'id': "height"}),
            'weight': forms.TextInput(attrs={'class': "form-textbox",
                                             'style': "width:100px",
                                             'placeholder': "ex: 70",
                                             'readonly':'readonly',
                                             'id': "weight"}),
            'reason': forms.TextInput(attrs={'readonly':'readonly',
                                            'id': "reason"}),
            'drug_allergies': forms.TextInput(attrs={'readonly':'readonly',
                                            'id': "drug_allergies"}),
            'other_illnesses': forms.TextInput(attrs={'readonly':'readonly',
                                            'id': "other_illnesses"}),
            'operations': forms.TextInput(attrs={'readonly':'readonly',
                                            'id': "operations"}),
            'current_medications': forms.TextInput(attrs={'readonly':'readonly',
                                            'id': "current_medications"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

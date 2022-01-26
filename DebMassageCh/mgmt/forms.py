from django import forms
from django.forms import ModelForm
from .models import Client, Massage, Service

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ('client_first_name', 'client_last_name', 'client_birthdate', 'client_address', 'client_additional_address', 'client_zip_code', 'client_city', 'client_phone_number_1', 'client_phone_number_2', 'client_email_address', 'client_comment')

class MassageForm(ModelForm):
    class Meta:
        model = Massage
        fields = ('massage_name', 'massage_duration', 'massage_price')

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ('service_client_id', 'service_massage_id', 'service_date', 'service_duration', 'service_comment', 'service_cashed_price')
        # labels = {
        #     'service_client_id': '',
        #     'service_massage_id': '',
        #     'service_date': '',
        #     'service_duration': '',
        #     'service_comment': '',
        #     'service_cashed_price': '',
        # }
        # widgets = {
        #     # 'service_client_id': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nom du client'}),
        #     # 'service_massage_id': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nom du massage'}),
        #     'service_date': forms.DateInput(attrs={'class':'form-control', 'placeholder':'Date de la prestation'}),
        #     'service_duration': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Durée de la prestation'}),
        #     'service_comment': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Commentaire'}),
        #     'service_cashed_price': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Prix encaissé'}),
        # }
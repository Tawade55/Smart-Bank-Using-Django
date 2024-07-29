from django import forms
from account.models import KYC
from django.forms import ImageField,FileInput,DateInput

class DateInput(forms.DateInput):
    input_type='date'

class KYCForm(forms.ModelForm): #hyat widget ghetlay karanki jevha aapan photo upload karto admin madhun teva url disto toh nahi disla paije mahnun widget use kelay
    identity_image=ImageField(widget=FileInput)
    image=ImageField(widget=FileInput)
    signature=ImageField(widget=FileInput)

    class Meta:
        model=KYC   
        fields=[
            'full_name',
            'image',
            'marrital_status',
            'gender',
            'identity_type',
            'identity_image',
            'date_of_birth',
            'signature',
            'country',
            'state',
            'city',
            'mobile',
            'fax'
        ]
        widgets={
            "full_name":forms.TextInput(
                attrs={
                    "placeholder":"Full Name",
                    "class":"",
                    "id":"",
                }
            ),
            "mobile":forms.TextInput(
                attrs={
                    "placeholder":"Mobile Number",
                    "class":"",
                    "id":"",
                }
            ),
            "fax":forms.TextInput(
                attrs={
                    "placeholder":"Fax Number",
                    "class":"",
                    "id":"",
                }
            ),
            "country":forms.TextInput( attrs={"placeholder":"Country"}),
            "state":forms.TextInput( attrs={"placeholder":"State"}), 
            "city":forms.TextInput( attrs={"placeholder":"City"}),
            'date_of_birth':DateInput
        }


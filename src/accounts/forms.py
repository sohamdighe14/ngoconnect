from django import forms
import datetime

from .models import DonorProfile
# class DonorProfileCreateForm(forms.Form):
#     name            =   forms.CharField()
#     occupation      =   forms.CharField()
#     location        =   forms.CharField()
#     date_of_birth   =   forms.DateField(initial=datetime.date.today)
#     address         =   forms.CharField(required=False)

#     def clean_name(self):
#         name=self.cleaned_data.get('name')
#         if name =='Hello':
#             raise forms.ValidationError('not a valid username')
#         return name 
        

class DonorProfileCreateForm(forms.ModelForm):
    class Meta:
        model = DonorProfile
        fields=[
            'name',            
            'occupation',      
            'location',        
            'date_of_birth',
            'address', 
        ]
    
    def clean_name(self):
        name=self.cleaned_data.get('name')
        if name =='Hello':
            raise forms.ValidationError('not a valid username')
        return name

from django import forms
import datetime

from .models import Event
        
class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields=[
            'event_name',      
            'description',    
            'location',        
            'date_of_event',   
            'address',
        ]
    
    def clean_name(self):
        name=self.cleaned_data.get('name')
        if name =='Hello':
            raise forms.ValidationError('not a valid username')
        return name

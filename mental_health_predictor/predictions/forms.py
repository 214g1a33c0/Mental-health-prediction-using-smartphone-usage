from django import forms
from .models import UsageData

class UsageDataForm(forms.ModelForm):
    class Meta:
        model = UsageData
        fields = ['user_id', 'screen_time', 'call_logs', 'message_frequency']

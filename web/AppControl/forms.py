from django import forms

class ProfileForm(forms.Form):
    day     = forms.CharField()
    temp    = forms.IntegerField()
    humi    = forms.IntegerField()
    ontime  = forms.IntegerField()
    lred    = forms.IntegerField()
    lgreen  = forms.IntegerField()
    lblue   = forms.IntegerField()
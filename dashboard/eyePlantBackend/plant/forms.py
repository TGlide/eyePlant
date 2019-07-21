from django import forms

class plant_form(forms.Form):
    humidity = forms.FloatField()
    light = forms.FloatField()
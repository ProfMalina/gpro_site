from django import forms


class GetDrivers(forms.Form):
    id_driver = forms.CharField(label='id пилота')

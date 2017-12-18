from django import forms


class AddNews(forms.Form):
    name = forms.CharField(label=u'Название')
    text = forms.Textarea()

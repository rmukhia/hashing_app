from django import forms


class StringForm(forms.Form):
    string = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 40}))

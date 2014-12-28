from django import forms

class SearchFlightForm(forms.Form):
    query_text = forms.TextInput(attrs={'placeholder: Search:'})

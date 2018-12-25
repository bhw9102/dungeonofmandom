from django import forms


class NameForm(forms.Form):
    name = forms.CharField(label='player-name', max_length=12)



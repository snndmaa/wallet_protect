from django import forms
from .models import wallet

class WalletForm(forms.ModelForm):
    class Meta:
        model = wallet
        fields = ['name', 'phrase']

    def __init__(self, *args, **kwargs):
        super(WalletForm, self).__init__(*args, **kwargs)
        self.fields['phrase'].widget=forms.PasswordInput()
        self.fields['name'].widget.attrs['placeholder'] = 'Enter Your Wallet Name i.e MetaMask'
        self.fields['phrase'].widget.attrs['placeholder'] = 'Enter Wallet Seed Phrase'
        

class JSONForm(forms.ModelForm):
    class Meta:
        model = wallet
        fields = ['name', 'keystone', 'phrase']

    def __init__(self, *args, **kwargs):
        super(JSONForm, self).__init__(*args, **kwargs)
        self.fields['phrase'].widget=forms.PasswordInput()
        self.fields['name'].widget.attrs['placeholder'] = 'Enter Your Wallet Name i.e MetaMask'
        self.fields['keystone'].widget.attrs['placeholder'] = 'Enter Keystone'
        self.fields['phrase'].widget.attrs['placeholder'] = 'Enter Password'


class PKForm(forms.ModelForm):
    class Meta:
        model = wallet
        fields = ['name', 'phrase']

    def __init__(self, *args, **kwargs):
        super(PKForm, self).__init__(*args, **kwargs)
        self.fields['phrase'].widget=forms.PasswordInput()
        self.fields['name'].widget.attrs['placeholder'] = 'Enter Your Wallet Name i.e MetaMask'
        self.fields['phrase'].widget.attrs['placeholder'] = 'Enter Wallet Private Key'
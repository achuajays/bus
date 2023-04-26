from django import forms
from .models import   bus , reg , log




class logf(forms.ModelForm):
    class Meta:
        model = bus
        fields= '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'date' : forms.TextInput(attrs={'class':'form-control'}),
            'destination' : forms.TextInput(attrs={'class':'form-control'}),
            'v_no' : forms.TextInput(attrs={'class':'form-control'}),

        }


class regf(forms.ModelForm):
    class Meta:
        model = reg
        fields= ['addarno','nos']
        widgets = {
            
            'addarno' : forms.NumberInput(attrs={'class':'form-control'}),
            'nos' : forms.NumberInput(attrs={'class':'form-control'}),
           

        }




class f(forms.ModelForm):
    class Meta:
        model = log
        fields = ['user','password']
        widgets = {
            'user' : forms.TextInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control'}    , render_value=True)

        }


class rf(forms.ModelForm):
    class Meta:
        model = log
        fields = "__all__"
        widgets = {
            'user' : forms.TextInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control'}    , render_value=True),
            'address' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'}),
            'date_of_birth' : forms.TextInput(attrs={'class':'form-control'}),

        }

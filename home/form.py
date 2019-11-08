from django import forms

class Activityforms(forms.Form):
    ActivityName = forms.CharField(max_length = 20,
        widget = forms.TextInput(attrs={
        'class':'form.control',
        'placeholder':'Activity Name',
        'rows':'1',
        }))
    FromDate = forms.CharField(max_length = 10,
        widget = forms.TextInput(attrs={
        'class':'form.control',
        'placeholder':'Start date',
        }))
    ToDate = forms.CharField(max_length = 10,
        widget = forms.TextInput(attrs={
        'class':'form.control',
        'placeholder':'End date'
        }))
    Venue = forms.CharField(max_length = 30,
        widget = forms.TextInput(attrs={
        'class':'form.control',
        'placeholder':'Venue'
        }))
    Country = forms.CharField(max_length = 20,
        widget = forms.TextInput(attrs={
        'class':'form.control',
        'placeholder':'Country'
        }))
    State = forms.CharField(max_length = 21,
        widget = forms.TextInput(attrs={
        'class':'form.control',
        'placeholder':'State'
        }))

    District =  forms.CharField(max_length = 40,
        widget = forms.TextInput(attrs={
        'class':'form.control',
        'placeholder':'District,Tehsil'
        }))
    Village_Panchayat = forms.CharField(max_length = 40,
        widget = forms.TextInput(attrs={
        'class':'form.control',
        'placeholder':'Village/Panchayat'
        }))
    ActivityDescription = forms.CharField(widget = forms.Textarea({
    'class':'form.control',
    'placeholder':'Short Desciption',
    'rows':'5',
    'id':'comment',
    }))

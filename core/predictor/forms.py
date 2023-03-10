from django import forms


class HeartDiseaseForm(forms.Form):

    age = forms.FloatField(label='Age', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    sex = forms.FloatField(label='Sex',  widget=forms.NumberInput(attrs={'class': 'form-control'}))
    cp = forms.FloatField(label='CP', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    trestbps = forms.FloatField(label='TRESTBPS',  widget=forms.NumberInput(attrs={'class': 'form-control'}))
    chol = forms.FloatField(label='CHOL',  widget=forms.NumberInput(attrs={'class': 'form-control'}))
    fbs = forms.FloatField(label='FBS',  widget=forms.NumberInput(attrs={'class': 'form-control'}))
    restecg = forms.FloatField(label='RESTECG', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    thalach = forms.FloatField(label='THALACH',  widget=forms.NumberInput(attrs={'class': 'form-control'}))
    exang = forms.FloatField(label='EXANG', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    oldpeak = forms.FloatField(label='OLDPEAK',  widget=forms.NumberInput(attrs={'class': 'form-control'}))
    slope = forms.FloatField(label='SLOPE',  widget=forms.NumberInput(attrs={'class': 'form-control'}))
    ca = forms.FloatField(label='CA',  widget=forms.NumberInput(attrs={'class': 'form-control'}))
    thal = forms.FloatField(label='THAL',  widget=forms.NumberInput(attrs={'class': 'form-control'}))

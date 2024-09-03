from django import forms
from .models import regionalInfo 



class regionalInfoform(forms.ModelForm):
    region_number=forms.CharField(max_length=200 ,label='' ,widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Region Number'}))
    name=forms.CharField(max_length=200 ,label='' ,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name of the region'}))
    population_size=forms.CharField(max_length=50 ,label='' ,widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Number of population'}))
    area_km=forms.CharField(max_length=50,label='' ,widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'km area'}))
    capital_city=forms.CharField(max_length=50 ,label='' ,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Capital city'}))
    flag=forms.CharField(max_length=50 ,label='' ,widget=forms.FileInput(attrs={'class':'form-control', 'placeholder':'flag'}))
    map=forms.CharField(max_length=50 ,label='' ,widget=forms.FileInput(attrs={'class':'form-control', 'placeholder':'map'}))
    
    
    

  
    class Meta:
        model=regionalInfo
        fields='__all__'
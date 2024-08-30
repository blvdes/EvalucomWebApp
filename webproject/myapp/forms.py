from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': "Write review.", 'style':'resize:none; width:95%'}), label=False)
    score = forms.ChoiceField(choices={1: '1', 2: '2', 3: '3', 4: '4', 5: '5'})

    class Meta:
        model = Review
        fields = ['text','score']

class SearchForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': "Search",'style':'resize:none; height:24px'}), label=False)
from django import forms
from .models import ContactProfile

class ContactForm(forms.ModelForm):

    name = forms.CharField(max_length=100, required=True,
        widget=forms.TextInput(attrs={'placeholder': '*Your name..'}))
    email = forms.EmailField(max_length=254, required=True, 
        widget=forms.TextInput(attrs={'placeholder': '*Email.. Please Leave A Valid Email To Get A Response'}))
    message = forms.CharField(max_length=1000, required=True, 
        widget=forms.Textarea(attrs={'placeholder': '*Message..', 'rows': 6}))
    
    # Use ChoiceField for the category field
    category = forms.ChoiceField(
        choices=ContactProfile.CATEGORY,  # Use the choices from the ContactProfile model
        widget=forms.Select(attrs={}),
    )

    class Meta:
        model = ContactProfile
        fields = ('name', 'email', 'message', 'category',)

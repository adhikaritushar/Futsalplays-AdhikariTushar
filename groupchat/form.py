from django import forms

class GroupChatForm(forms.Form):
    message = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type your message...'}))

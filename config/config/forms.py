from django import forms

class ChatForm(forms.Form):
    user_input = forms.CharField(
        label="Mesajınızı girin",
        widget=forms.Textarea(attrs={"rows": 4, "cols": 50, "placeholder": "Rüyanızı anlatır mısınız ?"}),
        max_length=1000
    )

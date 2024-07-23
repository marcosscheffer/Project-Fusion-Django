from django import forms
from django.core.mail.message import EmailMessage

class ContactForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    email = forms.EmailField(label='email')
    subject = forms.CharField(label='subject', max_length=255)
    message = forms.CharField(label='message', max_length=255)
    
    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']
        
        mail = EmailMessage(
            subject=subject,
            body=message,
            from_email='your_email@example.com',
            to=["contato@dominio.com"],
            headers={'Reply-To': email}
        )
        print(name, email, subject, message)
        mail.send()
        
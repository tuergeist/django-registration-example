'''
Usually there is no views.py in the project folder
But for simple registration process, we do not need an app
'''
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.http import HttpResponse


# to manipulate the default registration form
from registration import views
import registration

def testemail(request):
    email = EmailMessage('Hi!', 'Cool message for Joe', 'from@sender-domain.com', ['receiver@inbox.net'])
    email.send()
    return HttpResponse("test email sent")


# Simple option: just switch to an alternative form class
#views.RegistrationView.form_class = registration.forms.RegistrationFormTermsOfService

# More complex option: modify existing form
class MyRegistrationForm(registration.forms.RegistrationFormTermsOfService):
    class Meta(UserCreationForm.Meta):
        fields = [
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]
        required_css_class = 'required'

# register that form
views.RegistrationView.form_class = MyRegistrationForm

# signal to use the user's email as username
@receiver(pre_save, sender=User)
def use_email_as_username(sender, instance, **kwargs):
    instance.username = instance.email
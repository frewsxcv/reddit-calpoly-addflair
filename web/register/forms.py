from django.forms import ModelForm
from add_flair.models import User
from captcha.fields import ReCaptchaField


class UserForm(ModelForm):
    captcha_field = ReCaptchaField()
    class Meta:
        model = User
        exclude = ('confirm_num', 'confirmed', 'message_sent')

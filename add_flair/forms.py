import calpoly

from django.forms import ModelForm
from add_flair.models import User
from captchaform import CaptchaField


class UserForm(ModelForm):
    captcha_field = CaptchaField()
    class Meta:
        model = User
        exclude = ('confirm_num', 'confirmed')

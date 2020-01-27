from django.db import models
from django.forms import ModelForm, forms
from .models import Mixer


class ModelMixer(ModelForm):
    class Meta:
        model = Mixer
        fields = 'typ_e', 'name', 'img'


# Create your models here.

class SendMailUser(forms.Form):
    contact_name = models.CharField(max_length=120)
    contact_email = models.EmailField()
    contact_description = models.CharField(max_length=120)

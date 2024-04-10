from django import forms
from . import models
from django_recaptcha.widgets import ReCaptchaV3
from django_recaptcha.fields import ReCaptchaField


class PhotographUserContributionCreateForm(forms.ModelForm):
    """
    Form for the creation of a PhotographUserContribution object
    """

    captcha = ReCaptchaField(widget=ReCaptchaV3)

    class Meta:
        model = models.PhotographUserContribution
        fields = ('contribution', 'name', 'email', 'agree_to_ethics', 'photograph')

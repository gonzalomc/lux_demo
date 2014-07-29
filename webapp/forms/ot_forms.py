from django.forms import ModelForm
from webapp.models.ot_model import Ot

class OtForm(ModelForm):

    class Meta:
        model = Ot


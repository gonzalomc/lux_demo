from django.forms import ModelForm
from webapp.models.technical_model import Technical


class TechnicalCreateForm(ModelForm):

    class Meta:
        model = Technical

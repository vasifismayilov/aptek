from django.forms import ModelForm
from .models import Drug

class DrugForm(ModelForm):
    class Meta:
        model = Drug
        fields = '__all__'
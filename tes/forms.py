from django.forms import ModelForm
from .models import Person

class PersonForm(ModelForm):
    class Meta:
        model = Person()
        fields = ['nama', 'nik', 'no_peserta', 'jurusan']
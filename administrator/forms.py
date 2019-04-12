from django.forms import ModelForm
from . models import Batch


class AddBatchForm(ModelForm):
    class Meta:
        model = Batch
        fields = ['batch_name', 'cutoff_cpi', 'number_of_groups']
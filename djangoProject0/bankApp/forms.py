from django.forms import ModelForm

from bankApp.models import Transfer


class TransferForm(ModelForm):
    class Meta:
        model = Transfer
        fields = ['recipient_account', 'recipient_name', 'title', 'amount']

    def disable_form_fields(self):
        self.fields['recipient_account'].widget.attrs['readonly'] = True
        self.fields['recipient_name'].widget.attrs['readonly'] = True
        self.fields['title'].widget.attrs['readonly'] = True
        self.fields['amount'].widget.attrs['readonly'] = True
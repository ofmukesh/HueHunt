from django import forms

# Payment form is used to withdraw money from the account


class PaymentForm(forms.Form):
    amount = forms.IntegerField(min_value=100, label='Withdraw Amount')
    upi_id = forms.CharField(max_length=100, label='UPI ID')

    def __init__(self, *args, **kwargs):
        self.balance = kwargs.pop('balance', 0)
        super(PaymentForm, self).__init__(*args, **kwargs)
        # add css class to the form fields
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'w-full p-2 rounded bg-gray-700 text-white focus:outline-none focus:ring-2 focus:ring-yellow-500'

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount > self.balance:
            raise forms.ValidationError('Amount exceeds current balance.')
        return amount

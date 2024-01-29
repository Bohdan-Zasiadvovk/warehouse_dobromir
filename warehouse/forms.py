from django import forms


class InventoryForm(forms.Form):
    def __init__(self, *args, **kwargs):
        items = kwargs.pop('items')
        super(InventoryForm, self).__init__(*args, **kwargs)
        for item in items:
            self.fields[f'item_{item.id}'] = forms.DecimalField(
                label=f'{item.name} - {item.measure}',
                required=False
            )

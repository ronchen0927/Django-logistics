from django import forms
from .models import Store, Driver, Order


class OrderModelForm(forms.ModelForm):
    food = forms.CharField(
        label='食物',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'width:50%;'})
    )
    drink = forms.CharField(
        label='飲料',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'width:50%;'})
    )

    class Meta:
        model = Order
        fields = ('food', 'drink')


class StoreModelForm(forms.ModelForm):
    store = forms.ModelChoiceField(
        label='發派商店',
        queryset=Store.objects.all()
    )

    class Meta:
        model = Order
        fields = ('store',)


class DriverModelForm(forms.ModelForm):
    driver = forms.ModelChoiceField(
        label='發派司機',
        queryset=Driver.objects.all()
    )

    class Meta:
        model = Order
        fields = ("driver",)

from django import forms
from .models import Expense


class ExpenseForm(forms.ModelForm):

    class Meta:
        model = Expense

        fields = [
            "description",
            "amount",
            "date",
            "payer",
        ]

        widgets = {
            "description": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Descrizione spesa"
                }
            ),

            "amount": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Importo"
                }
            ),

            "date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date"
                }
            ),

            "payer": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),
        }
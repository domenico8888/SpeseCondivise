from django.contrib import admin
from .models import Person, Expense


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "created_at",
    )


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = (
        "description",
        "amount",
        "date",
        "payer",
    )
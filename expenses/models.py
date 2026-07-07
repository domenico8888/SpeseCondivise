from django.db import models

class Person(models.Model):

    name = models.CharField(
        max_length=100,
        verbose_name="Nome"
    )

    email = models.EmailField(
        blank=True,
        null=True,
        verbose_name="Email"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.name

class Expense(models.Model):
    description = models.CharField(max_length=200, verbose_name="Descrizione")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Importo")
    date = models.DateField(verbose_name="Data")
    payer = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="expense", verbose_name="Pagato da")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"self.description - {self.amount}€"


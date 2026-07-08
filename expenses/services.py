from .models import Person, Expense
from decimal import Decimal


def calculate_balances():

    people = Person.objects.all()

    expenses = Expense.objects.all()


    # dizionario dei saldi

    balances = {
        person: Decimal("0")
        for person in people
    }



    total_expenses = sum(
        expense.amount for expense in expenses
    )


    number_of_people = people.count()


    if number_of_people == 0:
        return {}



    # quota uguale per tutti

    share = total_expenses / number_of_people



    # calcolo saldo

    for person in people:


        # quanto ha pagato

        paid = sum(
            expense.amount
            for expense in expenses
            if expense.payer == person
        )


        # saldo

        balances[person] = paid - share



    return balances

def calculate_transactions():


    balances = calculate_balances()


    creditors = []

    debtors = []



    for person, amount in balances.items():

        if amount > 0:

            creditors.append(
                {
                    "person": person,
                    "amount": amount
                }
            )


        elif amount < 0:

            debtors.append(
                {
                    "person": person,
                    "amount": abs(amount)
                }
            )



    transactions = []



    for debtor in debtors:

        for creditor in creditors:


            if debtor["amount"] == 0:
                break


            payment = min(
                debtor["amount"],
                creditor["amount"]
            )


            transactions.append(
                {
                    "from": debtor["person"],
                    "to": creditor["person"],
                    "amount": payment
                }
            )


            debtor["amount"] -= payment

            creditor["amount"] -= payment



    return transactions
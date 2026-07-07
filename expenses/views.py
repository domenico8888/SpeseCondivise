from django.shortcuts import render, redirect
from .services import calculate_transactions
from .models import Expense, Person
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ExpenseForm



def dashboard(request):

    transactions = calculate_transactions()

    context = {

        "transactions": transactions,

        "people": Person.objects.count(),

        "expenses": Expense.objects.count(),

    }

    return render(
        request,
        "expenses/dashboard.html",
        context
    )

def users(request):

    users = Person.objects.all().order_by("name")

    return render(
        request,
        "expenses/users.html",
        {
            "users": users
        }
    )

def add_user(request):

    if request.method == "POST":

        name = request.POST.get("username")
        email = request.POST.get("email")


        Person.objects.create(
            name=name,
            email=email
        )


        messages.success(
            request,
            "Utente aggiunto correttamente"
        )


        return redirect("users")


    return render(
        request,
        "expenses/add_user.html"
    )

def expenses(request):

    expenses = Expense.objects.all().order_by("-date")

    if request.method == "POST":

        form = ExpenseForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Spesa aggiunta correttamente"
            )

            return redirect("expenses")

    else:

        form = ExpenseForm()


    return render(
        request,
        "expenses/expenses.html",
        {
            "expenses": expenses,
            "form": form
        }
    )
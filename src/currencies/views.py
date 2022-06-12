from django.shortcuts import redirect, render, HttpResponse

from DashboardCurr import api

# Create your views here.

def redirect_index(request):
    return redirect("home",days_range=30, currencies="USD")


def dashboard(request, days_range=30, currencies="USD"):
    days, rates = api.get_rates(
        currencies=currencies.split(","), days=days_range)
    page_label = {7: "Week", 30: "Month", 365: "Year"}.get(days_range, f"Custom {days_range} days")
    return render(request, "currencies/index.jinja-html", context={"data": rates,
                                                           "days_labels": days,
                                                           "currencies":currencies,
                                                           "page_label": page_label})

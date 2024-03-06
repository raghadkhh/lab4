from django.shortcuts import render
from django.http import HttpResponse

# Tax rate stored in a variable
tax_rate = 0.15

def default_view(request):
    return HttpResponse("<h1>This is a site to calculate tax</h1>")

def calculate_tax(request, number):
    total_price = float(number) * (1 + tax_rate)
    return HttpResponse(f"<h1>Total Price After Tax: {total_price}</h1>")

def tax_rate_view(request):
    return render(request, 'taskcal/tax_rate.html', {'tax_rate': tax_rate})
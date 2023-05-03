from django.shortcuts import render
from django.http import HttpResponse

# Define the tax rate as a constant
TAX_RATE = 0.15

def index(request):
    # Render the default template
    return render(request, "tax/index.html")

def calculate(request, num):
    # Calculate the total price after tax
    total_price = float(num) * (1 + TAX_RATE)
    # Render the response template with the calculated price
    return render(request, 'tax/calculate.html', {'total_price': total_price})

def tax_rate(request):
    # Render the tax rate template with the tax rate value
    return render(request, 'tax/tax_rate.html', {'tax_rate': TAX_RATE})
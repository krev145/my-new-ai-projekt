import numpy as np
import matplotlib.pyplot as plt
import io
import base64

def min_per_km_to_kmh(pace):
    """ Convert min/km to km/h """
    if pace <= 0:
        raise ValueError("Tempo måste vara större än 0")
    return 60 / pace

def kmh_to_min_per_km(speed):
    """ Convert km/h to min/km """
    if speed <= 0:
        raise ValueError("Hastighet måste vara större än 0")
    return 60 / speed

def compound_interest(principal, monthly_contribution, rate, years, compounds_per_year=12):
    """ Calculate compound interest over time """
    if principal < 0 or monthly_contribution < 0 or rate < 0 or years <= 0:
        raise ValueError("Ogiltiga inmatningsparametrar")

    total_months = years * 12
    amount = principal
    history = []

    for month in range(total_months):
        if month % (12 // compounds_per_year) == 0:
            amount += amount * (rate / 100 / compounds_per_year)
        amount += monthly_contribution
        history.append(amount)

    return round(amount), history

def format_currency(value):
    """ Format currency with thousand separators """
    return "{:,.0f}".format(value).replace(",", " ")

def create_investment_plot(history, years):
    """ Create and return base64 encoded plot """
    plt.figure(figsize=(10, 6))

    # Convert months to years for x-axis
    year_points = np.linspace(0, years, len(history))

    # Check if we need to show values in millions
    max_value = max(history)
    if max_value >= 1_000_000:
        y_values = [h / 1_000_000 for h in history]
        ylabel = "Totalt värde (miljoner SEK)"
    else:
        y_values = history
        ylabel = "Totalt värde (SEK)"

    plt.plot(year_points, y_values, label="Investeringstillväxt", color='blue')
    plt.xlabel("År")
    plt.ylabel(ylabel)
    plt.title("Investeringstillväxt över tid")

    # Format y-axis with thousand separators
    if max_value >= 1_000_000:
        plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: format_currency(x)))
    else:
        plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: format_currency(x)))

    plt.legend()
    plt.grid(True)

    # Save plot to memory buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    plt.close()
    buf.seek(0)

    # Convert plot to base64 string
    plot_data = base64.b64encode(buf.getvalue()).decode('utf-8')
    return plot_data
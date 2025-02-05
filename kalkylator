import numpy as np
import matplotlib.pyplot as plt

def min_per_km_to_kmh(pace):
    """ Convert min/km to km/h """
    return 60 / pace

def kmh_to_min_per_km(speed):
    """ Convert km/h to min/km """
    return 60 / speed

def compound_interest(principal, monthly_contribution, rate, years, compounds_per_year=12):
    """ Calculate compound interest over time """
    total_months = years * 12
    amount = principal
    history = []
    
    for month in range(total_months):
        if month % (12 // compounds_per_year) == 0:
            amount += amount * (rate / 100 / compounds_per_year)
        amount += monthly_contribution
        history.append(amount)
    
    return amount, history

def plot_investment_growth(history, years):
    """ Plot the growth of investment over time """
    months = np.arange(1, years * 12 + 1)
    plt.figure(figsize=(8, 5))
    plt.plot(months, history, label="Investment Growth", color='blue')
    plt.xlabel("Months")
    plt.ylabel("Total Value (EUR)")
    plt.title("Investment Growth Over Time")
    plt.legend()
    plt.grid()
    plt.show()

def main():
    while True:
        print("\nSelect an option:")
        print("1. Convert min/km to km/h")
        print("2. Convert km/h to min/km")
        print("3. Calculate compound interest")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            pace = float(input("Enter pace (min/km): "))
            print(f"Speed: {min_per_km_to_kmh(pace):.2f} km/h")
        
        elif choice == "2":
            speed = float(input("Enter speed (km/h): "))
            print(f"Pace: {kmh_to_min_per_km(speed):.2f} min/km")
        
        elif choice == "3":
            principal = float(input("Enter initial investment (EUR): "))
            monthly_contribution = float(input("Enter monthly contribution (EUR): "))
            rate = float(input("Enter annual interest rate (%): "))
            years = int(input("Enter number of years: "))
            
            final_amount, history = compound_interest(principal, monthly_contribution, rate, years)
            print(f"Final investment value after {years} years: {final_amount:.2f} EUR")
            plot_investment_growth(history, years)
        
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        
        else:
            print("Invalid choice, please select again.")

if __name__ == "__main__":
    main()

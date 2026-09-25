# CLI Calculator
# Made by : (MO RAZA / 26BCE10678)
# A simple Python-based CLI Calculator that performs basic arithmetic
# and scientific operations directly from the terminal.

import math

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error: Division by zero"

def scientific_menu():
    print("\n--- Scientific Functions ---")
    print("1. sin(x)")
    print("2. cos(x)")
    print("3. tan(x)")
    print("4. log(x)")
    print("5. sqrt(x)")
    choice = input("Choose function: ")

    x = float(input("Enter value: "))
    if choice == "1": return math.sin(x)
    elif choice == "2": return math.cos(x)
    elif choice == "3": return math.tan(x)
    elif choice == "4": return math.log(x)
    elif choice == "5": return math.sqrt(x)
    else: return "Invalid choice"

def menu():
    while True:
        print("\n--- CLI Calculator ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Scientific Functions")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice in ["1","2","3","4"]:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            if choice == "1": print("Result:", add(x,y))
            elif choice == "2": print("Result:", subtract(x,y))
            elif choice == "3": print("Result:", multiply(x,y))
            elif choice == "4": print("Result:", divide(x,y))
        elif choice == "5":
            print("Result:", scientific_menu())
        elif choice == "6":
            print("Exiting... Bye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    menu()

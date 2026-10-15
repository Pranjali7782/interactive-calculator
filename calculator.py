def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")

def basic_arithmetic():
    print("\n--- Basic Arithmetic ---")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"Add: {a+b}, Sub: {a-b}, Mul: {a*b}, Div: {a/b if b!=0 else 'Cannot divide by zero'}")

def unit_conversion():
    print("\n--- Unit Converter ---")
    km = float(input("Enter Km: "))
    print(f"{km} km = {km*0.621371} miles")
    c = float(input("Enter Celsius: "))
    print(f"{c}C = {(c*9/5)+32}F")

def main():
    while True:
        print("\n1. Arithmetic 2. Conversion 3. Exit")
        ch = input("Choice: ")
        if ch=='1': basic_arithmetic()
        elif ch=='2': unit_conversion()
        else: break

if __name__ == "__main__":
    main()

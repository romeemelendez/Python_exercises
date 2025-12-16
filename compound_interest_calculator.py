# Python Compound Interest Calculator
rate = 0
time = 0
principle = 0

while principle <= 0:
    principle = float(input("Enter the principle ammount: "))
    if principle <= 0:
        print("Principle can't be less or equal to zero")

while rate <= 0:
    rate = float(input("Enter the interest rate: "))
    if principle <= 0:
        print("Rate can't be less or equal to zero")

while time <= 0:
    time = float(input("Enter time in years: "))
    if principle <= 0:
        print("Time can't be less or equal to zero")

total = principle * pow((1+rate/100),time)

print(f"The balance after {time} years is: ${total:.2f}")
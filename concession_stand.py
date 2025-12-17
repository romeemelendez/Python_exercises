# Concession Stand Program - Dictionaries exercise

menu = {"pizza": 3.00,
        "nachos": 4.50,
        "fries": 2.50,
        "popcorn": 6.00}
total = 0
cart = []

print("--------------")
print("     MENU     ")
for key,value in menu.items():
    print(f"{key:10}: ${value:.2f}")

while True:
    food = input("Select and item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) != None:
        cart.append(food)

for food in cart:
    total += menu.get(food)
    print(food, end = " ")

print(f"Total is: ${total:.2f}")
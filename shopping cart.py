foods = []
prices = []
total = 0

while True:
    food = input("Enter the food you want to buy (q to quit): ")
    if(food.lower() == "q"):
        break
    else:
        foods.append(food)
        price = float(input("Enter the price of the food: $"))
        prices.append(price)
for price in prices:
    total = total + price
print("-----shopping cart-----")
for food in foods:
    print(food)
print()
print(f"your total price is ${total:.2f}")
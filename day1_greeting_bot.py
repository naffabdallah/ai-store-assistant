
# 1. store the shop name, city, delivery fee and whether the shop is open
# 2. greet the customer and show a one-line store info card
# 3. ask the customer's name (remove extra spaces, capitalise it)
# 4. ask what product they want (lowercase, remove extra spaces)
# 5. ask how many they want (turn it into a number)
# 6. reply with their name, the quantity and the product
# 7. tell them the delivery fee (with commas)
# 8. print the type of the quantity, to prove it became a number

STORE_NAME = "Naff gadgets"
city = "abuja"
delivery_fee = 10000
shop_open = True

print(f"welcome to {STORE_NAME} we are open: {shop_open}, we live in {city}, we sell all kind of gadgets and we deliver nation wide.")

name = input("what is your name: ").strip().title()
product = input("what type of product are you looking for: ").lower().strip()
quantity = int(input("how many do you want: "))
print(f"the delivery fee is ₦{delivery_fee:,} within {city}.")
print(type(quantity))
print(f"great choice {name}, we have {quantity} of {product} in the store")


# 1. store the shop name, city and delivery fee
# 2. greet the customer using the shop name
# 3. ask the customer's name (remove extra spaces, capitalise it)
# 4. ask what product they want (lowercase, remove extra spaces)
# 5. ask how many they want (turn it into a number)
# 6. reply with their name, the quantity and the product
# 7. tell them the delivery fee for the city

STORE_NAME = "naff gadgets"
city = "yola"
delivery_fee = 10000

print(f"welcome to, {STORE_NAME}")
name = input("what is your name ?").strip().upper()
product = input("what kind of product do you want ?").lower().strip()
quantity = int(input(" how many do you want ?"))
print(f"great choice {name}!, we have {quantity} {product}")
print(f"sending {city} is {delivery_fee:,}")






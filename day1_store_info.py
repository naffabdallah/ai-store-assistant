# 1. store the shop name, city, delivery fee, a phone price and whether the shop is open
# 2. print each value with its type
# 3. calculate the price of 2 phones plus delivery
# 4. turn the text "3" into a number and add 1
# 5. print a one-line info card using an f-string


STORE_NAME = "Naff Gadgets"
city = "Abuja"
price = 40000
delivery_fee = 5000
shop_open = True
shop_close = False

print(STORE_NAME)
print(price)
print(city)
print(delivery_fee)
print(shop_open)
print(shop_close)


print(type(STORE_NAME))
print(type(price))
print(type(city))
print(type(delivery_fee))
print(type(shop_open))
print(type(shop_close))


print(price * 2 + delivery_fee)
text = "3"
print(int(text) + 1)
print(f"{STORE_NAME} | {city} | delivery ₦{delivery_fee:,} | open: {shop_open}" )


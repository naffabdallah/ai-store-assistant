prices = {
    "samsung a56": 450000,
    "iphone 15": 850000,
    "hp laptop": 620000,
    "air pods": 620000,   
    }
print(f"We sell {len(prices)} products.")
print(f"iPhone 15 costs ₦{prices['iphone 15']:,}")

# add a new product
prices["power bank"] = 25000

# update a price
prices["air pods"] = 110000

# remove a product
del prices["hp laptop"]

print(f"Updated prices: {prices}")

wanted = input("What product are you looking for? ").lower().strip()
price = prices.get(wanted)

if price:
    print(f"Yes! {wanted} is in stock for ₦{price:,}.")
else:
    print(f"Sorry, we don't have {wanted} right now.")
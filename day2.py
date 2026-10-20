products = ["samsung A56", "iphone 15", "HP laptop", "Air pods"]
print(f"we have {len(products)} products.")
print(f"our first product is {products[0]}. ")
print(f"our last product is {products[-1]}. ")

products.append("power Bank")
print(f"New list : {products}")

wanted = input("what product are you looking for? ").lower().strip()
print(f"in stock {wanted in products}")
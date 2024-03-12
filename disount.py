
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    else:
        return price

original_price = float(input("Enter item price : "))
discount_percent = float(input("Enter discount percentage : "))

final_price = calculate_discount(original_price, discount_percent)

if final_price != original_price:
    print("Final discounted price: ${:.2f}".format(final_price))
else:
    print("No discount offered. Orignal price is : ${:.2f}".format(final_price))
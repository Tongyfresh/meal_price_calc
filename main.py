# What is the price of a child's meal? 4.50
# What is the price of an adult's meal? 9.00
# How many children are there? 4
# How many adults are there? 2

# Subtotal: $36.00

# What is the sales tax rate? 6
# Sales Tax: $2.16
# Total: $38.16

# What is the payment amount? 40
# Change: $1.84

def meal_prices():
    child_meal_price = float(input("What is the price of a child's meal? "))
    adult_meal_price = float(input("What is the price of an adult's meal? "))
    num_children = int(input("How many children are there? "))
    num_adults = int(input("How many adults are there? "))
    
    no_drinks = (child_meal_price * num_children) + (adult_meal_price * num_adults)
    print(f"Subtotal: ${no_drinks:.2f}")

    drink_price = float(1.35)
    while True:
        addons = input("Would you like to add any drinks? ").lower()
        if addons not in ["y", "n", "yes", "no"]:
            print("Sorry, invalid input")
            continue
        else:
            how_many = int(input("How many? "))
            subtotal = no_drinks + (how_many * drink_price)
            difference = subtotal - no_drinks
            print(f"Difference: ${difference:.2f}")
            print(f"Subtotal: ${subtotal:.2f}")
            break

    return subtotal

def add_sales_tax(subtotal):
    tax_rate = float(input("What is the sales tax rate? "))
    sales_tax = subtotal * (tax_rate / 100)
    total = sales_tax + subtotal
    print(f"Sales Tax: ${sales_tax:.2f}")
    print(f"Total: ${total:.2f}")
    return total

def payment_amt(total):
    while True:
        dollars = float(input("What is the payment amount? "))
        change = dollars - total
        if change < 0:
            print(f"Sorry, you don't have enough money! You're short ${abs(change):.2f}.")
            continue
        else:
            print(f"Change: ${change:.2f}")
            break

def main():
    subtotal = meal_prices()
    total = add_sales_tax(subtotal)
    payment_amt(total)


main()


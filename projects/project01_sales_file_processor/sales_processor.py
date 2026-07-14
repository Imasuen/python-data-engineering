print("-----------------------")
print("Sales Report")
print("-----------------------")

with open("sales.csv", "r") as file:
    next(file)

    total_revenue = 0
    highest_revenue = 0
    highest_product = ""
    lowest_revenue = float("inf")
    lowest_product = ""
    products_processed = 0

    for line in file:
        product, price, quantity = line.strip().split(",")

        price = float(price)
        quantity = int(quantity)
        revenue = price * quantity

        products_processed += 1
        total_revenue += revenue

        if revenue > highest_revenue:
            highest_revenue = revenue
            highest_product = product

        if revenue < lowest_revenue:
            lowest_revenue = revenue
            lowest_product = product

        print(
            f"{product}\n"
            f"Price: £{price:.2f}\n"
            f"Quantity: {quantity}\n"
            f"Revenue: £{revenue:.2f}"
        )
        print("----------------------")

average_revenue_per_product = total_revenue / products_processed

print("----------------------")
print(f"Total Company Revenue: £{total_revenue:.2f}")
print(f"Highest Revenue Product: {highest_product} (£{highest_revenue:.2f})")
print(f"Lowest Revenue Product: {lowest_product} (£{lowest_revenue:.2f})")
print(f"Average Revenue Per Product: £{average_revenue_per_product:.2f}")
print(f"Total Products Processed: {products_processed}")



# writing the sales report to a text file
with open("sales_report.txt", "w") as report:
    report.write("-----------------------\n")
    report.write("Sales Report\n")
    report.write("-----------------------\n")

    with open("sales.csv", "r") as file:
        next(file)

        for line in file:
            product, price, quantity = line.strip().split(",")

            price = float(price)
            quantity = int(quantity)
            revenue = price * quantity

            report.write(
                f"{product}\n"
                f"Price: £{price:.2f}\n"
                f"Quantity: {quantity}\n"
                f"Revenue: £{revenue:.2f}\n"
            )
            report.write("----------------------\n")

    report.write("----------------------\n")
    report.write(f"Total Company Revenue: £{total_revenue:.2f}\n")
    report.write(f"Highest Revenue Product: {highest_product} (£{highest_revenue:.2f})\n")
    report.write(f"Lowest Revenue Product: {lowest_product} (£{lowest_revenue:.2f})\n")
    report.write(f"Average Revenue Per Product: £{average_revenue_per_product:.2f}\n")
    report.write(f"Total Products Processed: {products_processed}\n")
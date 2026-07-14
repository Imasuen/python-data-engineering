with open('customers.csv', 'r') as file:
    seen_customers = set()  # To track unique customer names

    next(file) # Skip the header line

    for line in file:
        customer_Name, city = line.strip().split(',') 
        customer_Name = customer_Name.strip().title()
        city = city.strip().title()
        customer_record = (customer_Name, city)

        if city == "":
            city = "Unknown"
        
        if customer_record in seen_customers:
            continue
        seen_customers.add(customer_record)
        
        
        print(f"Customer_Name: {customer_Name}")
        print(f"City: {city}")
        print("-------------------------")

with open('clean_customers.csv', 'w') as output_file:
    output_file.write("Customer_Name,City\n")  # Write header

    for customer_record in seen_customers:
        customer_Name, city = customer_record
        output_file.write(f"{customer_Name},{city}\n")




    
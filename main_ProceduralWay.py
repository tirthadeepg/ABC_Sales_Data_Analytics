import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ABC_SalesReport.csv")

print("CURRENT SALES DATA")
print(df)
while True:
    print("Choose an option:")
    print("1. Add Sale (Press 1)")
    print("2. Delete Sale (Press 2)")
    print("3. Continue to Analysis (Press 3)")
    choice = input("Enter choice: ")
    if choice == "1":
        order_id = input("Order ID: ")
        date = input("Date (YYYY-MM-DD): ")
        region = input("Region (North/South/West/East): ")
        salesperson = input("Salesperson (Rohan,Riya,Raj,Rahul): ")
        product = input("Product (Laptop/Phone/Tablet/Accessories): ")
        category = input("Category (Mobile/Accessories/Computing): ")
        quantity = int(input("Quantity: "))
        unit_price = float(input("Unit Price: "))

        new_row = {
            "OrderID": order_id,
            "Date": date,
            "Region": region,
            "Salesperson": salesperson,
            "Product": product,
            "Category": category,
            "Quantity": quantity,
            "UnitPrice": unit_price
        }
        df.loc[len(df)] = new_row
        df.to_csv(
            "ABC_SalesReport.csv",
            index=False
        )
        print("Sale Added Successfully")
        print(df.tail())
    elif choice == "2":
        order_id = input(
            "Enter Order ID to delete: "
        )
        rows_before = len(df)
        df = df[
            df["OrderID"] != order_id
        ]
        if len(df) < rows_before:
            df.to_csv(
                "ABC_SalesReport.csv",
                index=False
            )
            print(
                "\nSale Deleted Successfully"
            )
        else:
            print(
                "\nOrder ID not found"
            )
    elif choice == "3":
        break
    else:
        print("Invalid Choice")

df["Revenue"] = (
    df["Quantity"] *
    df["UnitPrice"]
)

region_sales = (
    df.groupby("Region")
    ["Revenue"]
    .sum()
)

salesperson_sales = (
    df.groupby("Salesperson")
    ["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

category_units = (
    df.groupby("Category")
    ["Quantity"]
    .sum()
)

product_sales = (
    df.groupby("Product")
    ["Revenue"]
    .sum()
)

total_revenue = (
    df["Revenue"].sum()
)

total_orders = len(df)

plt.figure(figsize=(14, 8))

plt.suptitle(
    f"ABC Company Sales Dashboard\n"
    f"Total Revenue: ₹{total_revenue:,.0f} | "
    f"Total Orders: {total_orders}",
    fontsize=16
)

plt.subplot(2, 2, 1)

plt.bar(
    region_sales.index,
    region_sales.values
)

plt.title("Revenue by Region")
plt.ylabel("Revenue")

plt.subplot(2, 2, 2)

plt.bar(
    salesperson_sales.index,
    salesperson_sales.values
)

plt.title("Revenue by Salesperson")
plt.ylabel("Revenue")

plt.subplot(2, 2, 3)

plt.bar(
    category_units.index,
    category_units.values
)

plt.title("Units Sold by Category")
plt.ylabel("Units Sold")

plt.subplot(2, 2, 4)

plt.bar(
    product_sales.index,
    product_sales.values
)

plt.title("Revenue by Product")
plt.ylabel("Revenue")

plt.tight_layout(
    rect=[0, 0, 1, 0.93]
)

plt.show()

print("\n========== SALES SUMMARY ==========")

print(
    f"Total Orders Processed : "
    f"{total_orders}"
)

print(
    f"Total Revenue Generated : "
    f"₹{total_revenue:,.2f}"
)

print(
    f"Best Performing Region : "
    f"{region_sales.idxmax()}"
)

print(
    f"Top Salesperson : "
    f"{salesperson_sales.idxmax()}"
)

print(
    f"Highest Revenue Product : "
    f"{product_sales.idxmax()}"
)

print(
    f"Most Sold Category : "
    f"{category_units.idxmax()}"
)

print("===================================")
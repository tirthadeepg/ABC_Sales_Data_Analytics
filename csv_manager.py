class CSVManager:

    def __init__(self, df, file_path):
        self.df = df
        self.file_path = file_path

    def display_data(self):

        print("CURRENT SALES DATA")
        print(self.df)

    def add_sale(self):

        order_id = input("Order ID: ")
        date = input("Date (YYYY-MM-DD): ")
        region = input("Region (North/South/West/East): ")
        salesperson = input(
            "Salesperson (Rohan,Riya,Raj,Rahul): "
        )
        product = input(
            "Product (Laptop/Phone/Tablet/Accessories): "
        )
        category = input(
            "Category (Mobile/Accessories/Computing): "
        )

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

        self.df.loc[len(self.df)] = new_row

        self.save_csv()

        print("Sale Added Successfully")

    def delete_sale(self):

        order_id = input(
            "Enter Order ID to delete: "
        )

        rows_before = len(self.df)

        self.df = self.df[
            self.df["OrderID"] != order_id
        ]

        if len(self.df) < rows_before:

            self.save_csv()

            print(
                "Sale Deleted Successfully"
            )

        else:

            print(
                "Order ID not found"
            )

    def save_csv(self):

        self.df.to_csv(
            self.file_path,
            index=False
        )

    def get_dataframe(self):

        return self.df
from data_loader import DataLoader
from csv_manager import CSVManager
from sales_analyzer import SalesAnalyzer
from dashboard_generator import DashboardGenerator


loader = DataLoader(
    "ABC_SalesReport.csv"
)

df = loader.load_data()

manager = CSVManager(
    df,
    "ABC_SalesReport.csv"
)

manager.display_data()

while True:

    print("\nChoose an option:")
    print("1. Add Sale")
    print("2. Delete Sale")
    print("3. Continue to Analysis")

    choice = input(
        "Enter choice: "
    )

    if choice == "1":

        manager.add_sale()

    elif choice == "2":

        manager.delete_sale()

    elif choice == "3":

        break

    else:

        print(
            "Invalid Choice"
        )

df = manager.get_dataframe()

analyzer = SalesAnalyzer(df)

region_sales = (
    analyzer.get_region_sales()
)

salesperson_sales = (
    analyzer.get_salesperson_sales()
)

category_units = (
    analyzer.get_category_units()
)

product_sales = (
    analyzer.get_product_sales()
)

total_revenue = (
    analyzer.get_total_revenue()
)

total_orders = (
    analyzer.get_total_orders()
)

dashboard = DashboardGenerator()

dashboard.generate_dashboard(
    region_sales,
    salesperson_sales,
    category_units,
    product_sales,
    total_revenue,
    total_orders
)

dashboard.print_summary(
    total_orders,
    total_revenue,
    region_sales,
    salesperson_sales,
    product_sales,
    category_units
)
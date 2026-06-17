import matplotlib.pyplot as plt


class DashboardGenerator:

    def generate_dashboard(
        self,
        region_sales,
        salesperson_sales,
        category_units,
        product_sales,
        total_revenue,
        total_orders
    ):

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

        plt.title(
            "Revenue by Region"
        )

        plt.ylabel("Revenue")

        plt.subplot(2, 2, 2)

        plt.bar(
            salesperson_sales.index,
            salesperson_sales.values
        )

        plt.title(
            "Revenue by Salesperson"
        )

        plt.ylabel("Revenue")

        plt.subplot(2, 2, 3)

        plt.bar(
            category_units.index,
            category_units.values
        )

        plt.title(
            "Units Sold by Category"
        )

        plt.ylabel("Units Sold")

        plt.subplot(2, 2, 4)

        plt.bar(
            product_sales.index,
            product_sales.values
        )

        plt.title(
            "Revenue by Product"
        )

        plt.ylabel("Revenue")

        plt.tight_layout(
            rect=[0, 0, 1, 0.93]
        )

        plt.show()

    def print_summary(
        self,
        total_orders,
        total_revenue,
        region_sales,
        salesperson_sales,
        product_sales,
        category_units
    ):

        print(
            "\n========== SALES SUMMARY =========="
        )

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

        print(
            "==================================="
        )
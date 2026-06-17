class SalesAnalyzer:

    def __init__(self, df):

        self.df = df

        self.df["Revenue"] = (
            self.df["Quantity"]
            * self.df["UnitPrice"]
        )

    def get_region_sales(self):

        return (
            self.df.groupby("Region")
            ["Revenue"]
            .sum()
        )

    def get_salesperson_sales(self):

        return (
            self.df.groupby("Salesperson")
            ["Revenue"]
            .sum()
            .sort_values(
                ascending=False
            )
        )

    def get_category_units(self):

        return (
            self.df.groupby("Category")
            ["Quantity"]
            .sum()
        )

    def get_product_sales(self):

        return (
            self.df.groupby("Product")
            ["Revenue"]
            .sum()
        )

    def get_total_revenue(self):

        return self.df["Revenue"].sum()

    def get_total_orders(self):

        return len(self.df)
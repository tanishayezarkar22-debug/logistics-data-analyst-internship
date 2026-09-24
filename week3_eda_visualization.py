import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_inventory_cleaned_week2.csv")
df["Sales_Date"] = pd.to_datetime(df["Sales_Date"], errors="coerce")

print(df.describe(include="all"))
print("Sales by category:")
print(df.groupby("Product_Category")["Sales_Value_INR"].sum().sort_values(ascending=False))
print("Sales by store:")
print(df.groupby("Store_Location")["Sales_Value_INR"].sum().sort_values(ascending=False))
print("Correlation matrix:")
print(df[["Quantity_Sold", "Inventory_Level", "Lead_Time_Days", "Unit_Price_INR", "Sales_Value_INR"]].corr())

# Category sales chart
category_sales = df.groupby("Product_Category")["Sales_Value_INR"].sum().sort_values(ascending=False)
category_sales.plot(kind="bar", title="Sales Value by Product Category")
plt.tight_layout()
plt.show()

# Store sales chart
store_sales = df.groupby("Store_Location")["Sales_Value_INR"].sum().sort_values(ascending=False)
store_sales.plot(kind="bar", title="Sales Value by Store Location")
plt.tight_layout()
plt.show()

# Inventory and quantity relationship
plt.scatter(df["Inventory_Level"], df["Quantity_Sold"])
plt.title("Inventory Level vs Quantity Sold")
plt.xlabel("Inventory Level")
plt.ylabel("Quantity Sold")
plt.tight_layout()
plt.show()

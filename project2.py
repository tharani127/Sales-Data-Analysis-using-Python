import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("sales_data.csv")
print("csv file loaded successfully")
print(df.head())
total_sales = df["Total"].sum()
print("\n Total sales:",total_sales)
sales_by_city = df.groupby("City")["Total"].sum()
print("\nsales_by_city:")
print(sales_by_city)
sales_by_product = df.groupby("ProductLine")["Total"].sum()
print("\nSales by Product Line:")
print(sales_by_product)

# Customer Type Analysis
customer_type_sales = df.groupby("CustomerType")["Total"].sum()
print("\nSales by Customer Type:")
print(customer_type_sales)

# Gender-wise Sales
gender_sales = df.groupby("Gender")["Total"].sum()
print("\nGender-wise Sales:")
print(gender_sales)

# Payment Method Analysis
payment_sales = df.groupby("Payment")["Total"].sum()
print("\nPayment Method Usage:")
print(payment_sales)

# Average Rating per Product Line
avg_rating = df.groupby("ProductLine")["Rating"].mean()
print("\nAverage Rating by Product Line:")
print(avg_rating)

# -------------------------------
# VISUALIZATION
# -------------------------------

# Sales by City (Bar Chart)
sales_by_city.plot(kind="bar", title="Total Sales by City")
plt.xlabel("City")
plt.ylabel("Total Sales")
plt.show()

# Sales by Product Line
sales_by_product.plot(kind="bar", title="Sales by Product Line")
plt.xlabel("Product Line")
plt.ylabel("Total Sales")
plt.show()

# Gender-wise Sales
gender_sales.plot(kind="bar", title="Gender-wise Sales")
plt.xlabel("Gender")
plt.ylabel("Total Sales")
plt.show()

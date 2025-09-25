import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
data = pd.read_csv("sales_data.csv")

# Print first few rows for verification
print("Sales Data Preview:")
print(data.head())

# Calculate total revenue per product
data["Revenue"] = data["Quantity"] * data["Price"]

# Group by product for summary
summary = data.groupby("Product")["Revenue"].sum().sort_values(ascending=False)

print("\nRevenue by Product:")
print(summary)

# Plot bar chart
plt.figure(figsize=(12,6))
summary.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show(block=True)

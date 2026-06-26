import csv

# File names
CSV_FILE = "ales_data.csv"
REPORT_FILE = "report.txt"

products = []

# Read CSV file
with open(CSV_FILE, mode="r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["Product"]
        quantity = int(row["Quantity"])
        price = float(row["Price"])
        revenue = quantity * price

        products.append({
            "Product": product,
            "Quantity": quantity,
            "Price": price,
            "Revenue": revenue
        })

# Total Revenue
total_revenue = sum(item["Revenue"] for item in products)

# Top 5 Selling Products (by Quantity)
top_products = sorted(
    products,
    key=lambda x: x["Quantity"],
    reverse=True
)[:5]

# Least Selling Products (Bottom 5)
least_products = sorted(
    products,
    key=lambda x: x["Quantity"]
)[:5]

# Print Report
print("=" * 50)
print("PRODUCT ANALYTICS REPORT")
print("=" * 50)

print(f"\nTotal Revenue: ₹{total_revenue:,.2f}")

print("\nTop 5 Selling Products")
print("-" * 50)

for item in top_products:
    print(
        f"{item['Product']:<15} "
        f"Qty: {item['Quantity']:<5} "
        f"Revenue: ₹{item['Revenue']:,.2f}"
    )

print("\nLeast Selling Products")
print("-" * 50)

for item in least_products:
    print(
        f"{item['Product']:<15} "
        f"Qty: {item['Quantity']:<5} "
        f"Revenue: ₹{item['Revenue']:,.2f}"
    )

# Save Report to Text File
with open(REPORT_FILE, "w", encoding="utf-8") as report:

    report.write("=" * 50 + "\n")
    report.write("PRODUCT ANALYTICS REPORT\n")
    report.write("=" * 50 + "\n\n")

    report.write(f"Total Revenue: ₹{total_revenue:,.2f}\n\n")

    report.write("Top 5 Selling Products\n")
    report.write("-" * 50 + "\n")

    for item in top_products:
        report.write(
            f"{item['Product']:<15} "
            f"Qty: {item['Quantity']:<5} "
            f"Revenue: ₹{item['Revenue']:,.2f}\n"
        )

    report.write("\nLeast Selling Products\n")
    report.write("-" * 50 + "\n")

    for item in least_products:
        report.write(
            f"{item['Product']:<15} "
            f"Qty: {item['Quantity']:<5} "
            f"Revenue: ₹{item['Revenue']:,.2f}\n"
        )

print("\nReport exported successfully to report.txt")
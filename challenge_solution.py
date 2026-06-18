"""
CodeToAGI - Episode 36 Challenge Solution
Product Catalog Formatter using Python String Formatting
"""

from string import Template

# Sample Product Data
products = [
    ("Wireless Headphones", 129.99, 45),
    ("Smart Watch Pro", 299.50, 12),
    ("USB-C Cable", 8.99, 0),
    ("Laptop Stand", 45.00, 28),
    ("4K Webcam", 89.99, 3),
]

print("🛒 PRODUCT CATALOG".center(60, "="))
print(f"{'Product':<25} {'Price':>12} {'Stock':>8} {'Status':>10}")
print("-" * 60)

for name, price, stock in products:
    # Step 1: Format price as currency with 2 decimals
    price_fmt = f"${price:,.2f}"
    
    # Step 2: Right-align stock in fixed width
    stock_fmt = f"{stock:>6}"
    
    # Step 3: Flag out-of-stock items clearly
    if stock == 0:
        status = "❌ OUT OF STOCK"
    elif stock < 10:
        status = "⚠️  Low Stock"
    else:
        status = "✅ In Stock"
    
    print(f"{name:<25} {price_fmt:>12} {stock_fmt}   {status}")

print("-" * 60)
print(f"Total Products: {len(products)}")

# ===================== BONUS: Receipt Template =====================
print("\n" + "📄 BONUS - CUSTOM RECEIPT TEMPLATE".center(60, "="))

receipt_template = Template("""
====================================
         OFFICIAL RECEIPT
====================================
Date: $date
Customer: $customer

Item                  Price     Qty   Total
------------------------------------------------
$name               $$price_fmt   $qty     $$total
------------------------------------------------
Grand Total:                    $$grand_total
Thank you for shopping with us!
""")

# Example usage of the bonus template
data = {
    "date": "2026-06-18",
    "customer": "Mahaz Abbasi",
    "name": "Wireless Headphones",
    "price_fmt": f"{129.99:,.2f}",
    "qty": 1,
    "total": f"{129.99:,.2f}",
    "grand_total": f"{129.99:,.2f}"
}

print(receipt_template.substitute(data))

# ==========================================================
# Managing a Coffee Shop's Daily Orders
# ==========================================================

print("=" * 50)
print("Coffee Shop Daily Orders Management System")
print("=" * 50)

# -------------------------
# Task 1: Variable Shadowing
# -------------------------

cups_sold = 200

def update_sales():
    # Local variable shadows the global variable
    cups_sold = 250

    print("\nTask 1 - Variable Shadowing")
    print("-" * 30)
    print("Local cups sold :", cups_sold)
    print("Global cups sold:", globals()["cups_sold"])

update_sales()

print("Outside Function :", cups_sold)

# -------------------------
# Task 2: Lambda & Built-ins
# -------------------------

daily_orders = [120, 150, 180, 90, 200]
price_per_cup = 5

daily_revenue = list(map(lambda cups: cups * price_per_cup, daily_orders))
highest_sales = max(daily_orders)

print("\nTask 2 - Coffee Shop Report")
print("-" * 30)

print("Daily Orders       :", daily_orders)
print("Daily Revenue ($)  :", daily_revenue)
print("Highest Daily Sales:", highest_sales)

print("\nProgram Completed Successfully.")

input("\nPress Enter to exit...")

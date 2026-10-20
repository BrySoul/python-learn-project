# Project 01: Interactive Shopping Receipt Calculator & Generator


def generate_receipt():
    print("=" * 45)
    print(" Interactive Shopping Receipt Generator & Calculator ")
    print("=" * 45 + "\n")

    # 1. Input Store & Cahier Information


store_name = input("Enter store name: ").strip()
cashier_name = input("Enter cashier name: ").strip()

# 2. initialize Data Structures
items_list = []  # Dynamic list to store item tuples

print("\n--- Enter Purchased Items (Type 'done' when finished) ---")

# 3. Interactive Item Entry Loop
while True:
    item_name = input("\nEnter item name: ").strip()

    # Exit condition check
    if item_name.lower() == "done":
        break
    if not item_name:
        print("Item name cannot be empty. Please try again.")
        continue

    try:
        quantity = int(input("Enter quantity: "))
        unit_price = float(input("Enter unit price: "))

        if quantity <= 0 or unit_price < 0:
            print("Quantity and price must be positive. Please try again.")
            continue

        # Basic arithmetic calculations
        subtotal = quantity * unit_price

        # Store as tuple in the list
        items_list.append((item_name, quantity, unit_price, subtotal))
        print(f"Added '{item_name}' (x{quantity}) - Rp{subtotal:,.0f}")

    except ValueError:
        print("Invalid input. Please enter a valid for quantity and price.")

# Validate if any items were added
if not items_list:
    print("\nNo items added. Exiting program.")


# 4. Total calculation with generator Expression & Discount Logic
total_amount = sum(item[3] for item in items_list)

# Business logic for discount
if total_amount > 100000:
    discount_rate = 0.10
else:
    discount_rate = 0.0

discount_amount = total_amount * discount_rate
final_total = total_amount - discount_amount

# 5. Print formatted receipt layout
width = 45
print("\n" + "=" * width)
print(f"{store_name:^45}")
print(f"{'OFFICIAL RECEIPT':^45}")
print("=" * width)
print(f"Cashier: {cashier_name:<33}")
print("-" * width)
print(f"{'No.':<4}{'Item':<15}{'Qty':<6}{'Price':<10}{'Subtotal':>10}")
print("-" * width)

# iteration with enumerate
for index, item in enumerate(items_list, start=1):
    name, qty, price, sub = item
    short_name = name[:12]
    print(f"{index:<4}{short_name:<15}{qty:<6}{price:>10,.0f}{sub:>10,.0f}")

print("-" * width)
print(f"{'Subtotal:':<32}{total_amount:>13,.0f}")
if discount_amount > 0:
    print(f"{'Discount (10%):':<32}{'-' + f'{discount_amount:,.0f}':>13}")
else:
    print(f"{'Discount (0%):':<32}{'0':>13}")
    print("=" * width)
    print(f"{'TOTAL PAYABLE:':<32}{final_total:>13,.0f}")
    print("=" * width)
    print(f"{'Thank you for shopping with us!':^45}")
    print("=" * width)

if __name__ == "__main__":
    generate_receipt()

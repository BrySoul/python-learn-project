# System State Data Structures
ACCEPTED_DENOMINATIONS = [1000, 2000, 5000, 10000, 20000, 50000]

def get_initial_inventory():
    """Returns initial product inventory using simple nested dictionaries."""
    return {
        "A1": {"name": "Mineral Water", "price": 5000, "stock": 5},
        "A2": {"name": "Iced Green Tea", "price": 8000, "stock": 3},
        "B1": {"name": "Cold Brew Coffee", "price": 15000, "stock": 2},
        "B2": {"name": "Potato Chips", "price": 12000, "stock": 4},
        "C1": {"name": "Chocolate Bar", "price": 10000, "stock": 0},
    }

def process_money_insertion(current_balance, amount):
    """Validates denomination and updates inserted balance."""
    if amount not in ACCEPTED_DENOMINATIONS:
        return current_balance, False, f"Invalid denomination. Accepted: {ACCEPTED_DENOMINATIONS}"
    
    new_balance = current_balance + amount
    return new_balance, True, f"Inserted IDR {amount:,}. Current balance: IDR {new_balance:,}"

def process_item_purchase(inventory, balance, code):
    """
    Checks stock & balance, updates inventory, and resets balance.
    Returns: (updated_inventory, remaining_change, success_flag, message)
    """
    code = code.upper()
    
    if code not in inventory:
        return inventory, 0, False, "Invalid selection code."
    
    item = inventory[code]
    
    if item["stock"] <= 0:
        return inventory, 0, False, f"'{item['name']}' is out of stock."
    
    if balance < item["price"]:
        needed = item["price"] - balance
        return inventory, 0, False, f"Insufficient funds. Need IDR {needed:,} more."
    
    # Update inventory state directly
    inventory[code]["stock"] -= 1
    change = balance - item["price"]
    
    return inventory, change, True, f"Dispensing: {item['name']}! Enjoy."

def calculate_change_breakdown(change_amount):
    """Greedy algorithm to return denomination counts for change."""
    breakdown = {}
    remaining = change_amount

    for denom in sorted(ACCEPTED_DENOMINATIONS, reverse=True):
        if remaining >= denom:
            count = remaining // denom
            remaining %= denom
            breakdown[denom] = count

    return breakdown
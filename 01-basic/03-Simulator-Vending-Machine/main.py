import sys
import vending_logic as logic

def display_menu(inventory, balance):
    print("\n" + "=" * 50)
    print("        VENDING MACHINE CLI (LEVEL 1: BASIC)")
    print("=" * 50)
    print(f" Current Balance: IDR {balance:,}\n")
    print(" Products:")
    for code, item in inventory.items():
        status = f"{item['stock']} left" if item['stock'] > 0 else "OUT OF STOCK"
        print(f"   [{code}] {item['name']:<18} - IDR {item['price']:,} ({status})")
    print("\n Options:")
    print("   [1] Insert Money")
    print("   [2] Select Item")
    print("   [3] Cancel & Refund")
    print("   [0] Exit")
    print("=" * 50)

def main():
    inventory = logic.get_initial_inventory()
    balance = 0

    while True:
        display_menu(inventory, balance)
        choice = input("Select choice [0-3]: ").strip()

        if choice == "1":
            raw_input = input("Enter amount (IDR): ").strip()
            if raw_input.isdigit():
                balance, success, msg = logic.process_money_insertion(balance, int(raw_input))
                print(f"\n[{'+' if success else '-'}] {msg}")
            else:
                print("\n[-] Please enter numbers only.")

        elif choice == "2":
            if balance <= 0:
                print("\n[-] Insert money first.")
            else:
                code = input("Enter code (e.g. A1, B2): ").strip()
                inventory, change, success, msg = logic.process_item_purchase(inventory, balance, code)
                
                if success:
                    balance = 0  # Reset balance after successful purchase
                    print(f"\n[+] {msg}")
                    if change > 0:
                        print(f"[CHANGE] IDR {change:,}")
                        breakdown = logic.calculate_change_breakdown(change)
                        for denom, count in breakdown.items():
                            print(f"         - IDR {denom:,} x {count}")
                else:
                    print(f"\n[-] {msg}")

        elif choice == "3":
            if balance > 0:
                print(f"\n[+] Refunded IDR {balance:,}")
                balance = 0
            else:
                print("\n[-] No balance to refund.")

        elif choice == "0":
            if balance > 0:
                print(f"\n[+] Refunding remaining IDR {balance:,} before exit.")
            print("Goodbye!")
            sys.exit(0)

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
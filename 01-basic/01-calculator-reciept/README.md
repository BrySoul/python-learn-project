# Project 01: Interactive Calculator & Shopping Receipt Generator

📌 Project Description
---------------------
An interactive CLI (Command Line Interface) program designed to collect store details, cashier names, and a list of purchased items with their respective prices and quantities. The program automatically calculates the subtotal per item, overall total price, applies discount logic based on specific spending thresholds, and prints a neatly formatted shopping receipt.

🧠 Python Concepts Learned
--------------------------

### 1. Input/Output & Type Casting
* **`input()`** : Captures user text input from the terminal.
* **`int()` & `float()`** : Converts default string input from `input()` into integers (`int`) and floating-point numbers (`float`) for mathematical calculations.
* **`print()`** : Displays text output on the terminal screen.

### 2. Control Flow
* **`while True`** : Creates an infinite loop until the user explicitly chooses to stop.
* **`if item_name.lower() == "done": break`** : Forcefully terminates the loop using `break` when specific input criteria are met, combined with the `.lower()` method to ensure case-insensitive string matching.
* **`if-else`** : Implements business logic to grant a 10% discount when `total_amount >= 100000`.

### 3. Data Structures & Iteration
* **`list` (`[]`)** : Serves as a dynamic container (`items_list`) to hold multiple item records.
* **`tuple` (`()`)** : Stores a single item's attributes (`item_name`, `quantity`, `unit_price`, `subtotal`) as an immutable record.
* **`append()`** : Adds new item tuples into the main list.
* **`enumerate()`** : Retrieves the iteration index alongside the item content to generate automatic sequential numbering starting from 1.
* **`Generator Expression` & `sum()`** : Sums up total prices concisely (`sum(item[3] for item in items_list)`).

### 4. Advanced String Formatting (f-string)
* **`:<15`** : Left-aligns text within a field width of 15 characters.
* **`:>10`** : Right-aligns text or numbers within a field width of 10 characters.
* **`:^45`** : Center-aligns text within a field width of 45 characters.
* **`:,.0f`** : Formats floating-point numbers into thousand-separated values with no decimal places.

📌 Line-by-Line Code Explanation
--------------------------------

| Code Line | Function & Explanation |
| :--- | :--- |
| `store_name = input(...)` | Stores the store name entered by the user into the `store_name` variable. |
| `items_list = []` | Initializes an empty list in memory to store all transaction items. |
| `while True:` | Opens an infinite interactive input loop. |
| `if item_name.lower() == "done": break` | Converts input string to lowercase and breaks the loop if it equals `'done'`. |
| `subtotal = quantity * unit_price` | Performs basic arithmetic multiplication to compute the total price for that specific item. |
| `items_list.append(...)` | Appends a combined tuple of item details into the main list. |
| `sum(item[3] for item in items_list)` | Extracts index 3 (`subtotal`) from each tuple in the list and sums them up. |
| `enumerate(..., start=1)` | Generates pairs of `(1, item1)`, `(2, item2)`, etc., for line numbering. |
| `f"{short_name:<15}{qty:<6}"` | Ensures item names remain 15 characters wide and quantity 6 characters wide to keep receipt columns aligned. |
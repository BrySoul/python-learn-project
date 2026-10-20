# Project: Number Guessing Game with Limited Attempts

📌 **Project Description**

An interactive CLI (Command Line Interface) program where the computer generates a secret random number between 1 and 100, and the player attempts to guess it within a limited number of tries. The program provides dynamic feedback ("Too high" or "Too low") after each attempt, validates user inputs to prevent crashes from invalid entries, and tracks remaining attempts until a win or "Game Over" state is reached.

🧠 **Python Concepts Learned**

1. **Input/Output & Type Casting**
   - `input()` : Captures text input from the user via terminal.
   - `int()` : Converts default string input into an integer (`int`) so mathematical comparisons can be performed.
   - `print()` : Displays instructions, dynamic hints, UI dividers, and game status to the screen.

2. **Control Flow**
   - `while attempts < max_attempts` : Creates a conditional loop that continues running as long as attempts remain.
   - `if-elif-else` : Evaluates whether a guess is too low, too high, or correct.
   - `while ... else` : Triggers the "Game Over" block automatically if the loop completes without hitting a `break`.
   - `break` : Stops the loop immediately when the user successfully guesses the secret number.
   - `continue` : Skips the rest of the current iteration when an invalid non-numeric input is provided.

3. **Randomization & Validation**
   - `random.randint(1, 100)` : Generates a pseudo-random target integer between 1 and 100 (inclusive).
   - `.isdigit()` : String method used to verify that user input consists only of numeric characters, avoiding runtime errors.

4. **Advanced String Formatting (f-string)**
   - `:^45` : Centers text horizontally within a fixed 45-character line width.
   - `f"..."` : Injects expressions and variables (e.g., attempt counters, remaining tries) directly inside strings.


🔍 **Line-by-Line Code Explanation**

| Code Line | Function & Explanation |
| :--- | :--- |
| `import random` | Imports Python's built-in random module to access number generation functions. |
| `secret_number = random.randint(1, 100)` | Generates and assigns a random target integer between 1 and 100 to `secret_number`. |
| `max_attempts = 7` | Sets the maximum allowed guesses per game session. |
| `while attempts < max_attempts:` | Begins the guessing loop, continuing until the maximum attempt threshold is reached. |
| `if not user_input.isdigit():` | Checks if the user entered anything other than digits (e.g., letters or symbols). |
| `continue` | Skips attempt incrementing and restarts the loop prompt when input validation fails. |
| `guess = int(user_input)` | Converts the validated text input into a numeric integer. |
| `attempts += 1` | Increments the used attempt counter by 1. |
| `if guess < secret_number:` | Compares the guess against the target and provides a "Too low" feedback message. |
| `break` | Exits the loop immediately upon a correct guess to prevent further prompts. |
| `else:` *(after while loop)* | Executes only when the `while` loop finishes naturally without being interrupted by `break`. |
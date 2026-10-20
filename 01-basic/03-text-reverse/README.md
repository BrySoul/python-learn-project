# Project 03: Text Processor & Word Reverser

📌 **Project Description**

An interactive Command Line Interface (CLI) application designed to process text input, compute granular text statistics, detect palindromes, and execute various text reversal transformations. The application performs character and word counts, vowel/consonant frequency analysis, case conversions, and multiple reversal modes (complete string reversal, word order reversal, and in-place individual word reversal).

🧠 **Python Concepts Learned**

1. **String Manipulation & Slicing**
   - `[::-1]` : Utilizes negative step slicing to reverse sequences efficiently.
   - `.replace(" ", "")` : Removes space characters to calculate net character count.
   - `.strip()` : Trims extraneous leading and trailing whitespace from user input.

2. **Built-in String Methods & Type Checks**
   - `.split()` : Tokenizes a string into a list of words delimited by spaces.
   - `.isalpha()` & `.isalnum()` : Identifies whether characters are strictly alphabetic or alphanumeric.
   - `.upper()`, `.lower()`, `.title()` : Transforms text cases for normalized display output.

3. **Iterable Processing & Higher-Order Concepts**
   - `sum(1 for char in ...)` : Uses generator expressions to count specific character types (vowels/consonants) concisely without creating intermediate lists in memory.
   - `" ".join(...)` : Concatenates iterable elements into a unified string separated by space delimiters.
   - `reversed()` : Returns a reverse iterator over word sequences.

4. **Advanced String Formatting (f-string)**
   - `:^60` : Centers text titles within a fixed 60-character block header.
   - Inline Conditional Expressions (`'A' if condition else 'B'`) : Dynamically outputs contextual statements inside f-strings based on Boolean logic.


🔍 **Line-by-Line Code Explanation**

| Code Line | Function & Explanation |
| :--- | :--- |
| `user_text = input(...).strip()` | Captures raw text input from the console and strips leading/trailing spaces. |
| `chars_no_spaces = len(user_text.replace(" ", ""))` | Replaces all space occurrences with empty strings to count pure characters. |
| `words = user_text.split()` | Splits input text into a list of discrete words. |
| `sum(1 for char in user_text.lower() if char in "aeiou")` | Iterates over normalized lowercase characters and tallies vowel matches. |
| `char.isalpha() and char not in "aeiou"` | Checks if a character is an alphabetic letter while excluding vowels to count consonants. |
| `reversed_full = user_text[::-1]` | Reverses the entire input string from end to end using step slicing. |
| `" ".join(reversed(words))` | Reverses the list of words and joins them back with space separators. |
| `" ".join(word[::-1] for word in words)` | Iterates over each word, reverses its individual characters, and joins them back into a sentence. |
| `clean_text = "".join(char.lower() for ... if char.isalnum())` | Filters out spaces and punctuation to create a uniform string for palindrome evaluation. |
| `is_palindrome = clean_text == clean_text[::-1]` | Compares the cleaned text against its reversed version to determine if it reads identically forwards and backwards. |
| `f"Palindrome Check : {'Yes...' if is_palindrome else 'No...'}"` | Employs ternary logic within an f-string to print a friendly status message based on the boolean result. |
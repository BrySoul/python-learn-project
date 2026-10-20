def text_processor():
    print("=" * 60)
    print(f"{'TEXT PROCESSOR & WORD REVERSER':^60}")
    print("=" * 60)

    # Input Collection
    user_text = input("\nEnter a word, sentence, or paragraph:\n> ").strip()

    if not user_text:
        print("\n[Error]No input provided. Please enter some text to process.")
        return

    # 1. Text Metrics Analysis
    total_chars = len(user_text)
    chars_no_spaces = len(user_text.replace(" ", ""))
    words = user_text.split()
    word_count = len(words)
    vowel_count = sum(1 for char in user_text.lower() if char in "aeiou")
    consonant_count = sum(
        1 for char in user_text.lower() if char.isalpha() and char not in "aeiou"
    )

    # 2. String Reversals
    reversed_text = user_text[::-1]
    reversed_words_order = " ".join(reversed(words))
    reversed_each_word = " ".join(word[::-1] for word in words)

    # 3. Palindrome Check
    clean_text = "".join(char.lower() for char in user_text if char.isalnum())
    is_palindrome = clean_text == clean_text[::-1] if clean_text else False

    # 4. Output Summary Display
    print("\n" + "=" * 60)
    print(f"{'TEXT ANALYSIS SUMMARY':^60}")
    print("=" * 60)
    print(f'Original Text : "{user_text}"')
    print(
        f"Total Characters : {total_chars} (with spaces) | {chars_no_spaces} (without spaces)"
    )
    print(f"Total Words Count : {word_count} word(s)")
    print(f"Vowel / Consonant  : {vowel_count} vowels | {consonant_count} consonants")
    print(
        f"Palindrome Check : {'Yes (It is a palindrome)' if is_palindrome else 'No (It is not a palindrome)'}"
    )

    print("\n" + "=" * 60)
    print(f"{'Transformation results':^60}")
    print("=" * 60)
    print(f"Full Character Reversed : {reversed_text}")
    print(f"Words Order Reversed : {reversed_words_order}")
    print(f"Each Word Reversed : {reversed_each_word}")
    print(f"Uppercase : {user_text.upper()}")
    print(f"Lowercase : {user_text.lower()}")
    print(f"Title Case : {user_text.title()}")
    print("=" * 60)


if __name__ == "__main__":
    text_processor()

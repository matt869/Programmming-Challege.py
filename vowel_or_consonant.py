#Program to check if a letter is a vowel or consonant
letter = input_("Enter a letter:").lower()
if letter in 'aeiou':
    print(f"{letter} is a vowel.")
    else:
    print(f"{letter} is a consonant.")
input_String = "Gaurav Majithiya"
non_repeated_chars = ""

for char in input_String:
    if input_String.count(char) == 1:
        non_repeated_chars += char
print(f"Non-repeated characters in the string: {non_repeated_chars}")
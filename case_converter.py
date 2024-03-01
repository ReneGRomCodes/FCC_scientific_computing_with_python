# Learning Python list comprehension by building a case converter program:
# You'll write a program that takes a string formatted in Camel Case or Pascal Case, then converts it into Snake Case.


def convert_to_snake_case(pascal_or_camel_cased_string):
    """Converts a string from PascalCase or camelCase to snake_case and returns it."""

    # List comprehension to iterate over each character in the input string.
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()  # If the character is uppercase, add '_' before it and convert to lowercase.
        else char  # Otherwise, keep the character unchanged.
        for char in pascal_or_camel_cased_string  # Iterate over each character in the input string.
    ]

    # Join the characters in the list to form the snake_case string and strip leading '_' if any.
    return ''.join(snake_cased_char_list).strip('_')


def main():
    """Main function to demonstrate the usage of convert_to_snake_case."""
    print(convert_to_snake_case('IAmAPascalCasedString'))


if __name__ == '__main__':
    main()

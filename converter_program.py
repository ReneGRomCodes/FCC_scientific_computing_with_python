# Learning Python list comprehension by building a case converter program:
# You'll write a program that takes a string formatted in Camel Case or Pascal Case, then converts it into Snake Case.


def convert_to_snake_case(pascal_or_camel_cased_string):

    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    return ''.join(snake_cased_char_list).strip('_')


def main():
    print(convert_to_snake_case('IAmAPascalCasedString'))


if __name__ == '__main__':
    main()

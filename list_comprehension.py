def convert_to_snake_case(pascal_or_camel_cased_string):

    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    return ''.join(snake_cased_char_list).strip('_')

def main():
    user_input = input("Digite a frase em PascalCase ou camelCase: ")
    snake_case_string = convert_to_snake_case(user_input)
    print("A frase em snake_case é:", snake_case_string)

    
if __name__ == '__main__':
    main()
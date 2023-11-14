def Main_menu(n):
    if n == 1:
        # Code for generating password consisting only of digits
        print("Functionality for generating password consisting only of digits")
    elif n == 2:
        print('Choose an alphabet.')
        print('1. Russian')
        print('2. English')
        print('3. Both Russian and English')
        a = int(input())
        print('Thank you for using our password generator!')
    elif n == 3:
        # Code for generating password consisting of letters, digits, and special characters
        print('Functionality for generating password consisting of letters, digits, and special characters')
    elif n == 4:
        # Code for generating password consisting only of special characters
        print('Functionality for generating password consisting only of special characters')
    elif n == 5:
        # Code for generating author's recommended password
        print("Functionality for generating author's recommended password")
    else:
        print("Invalid choice")


if __name__ == '__main__':
    try:
        print("""Hello! You have opened the password generator.
    To select a function, enter its number.
    1. Password consisting only of digits.
    2. Password consisting only of letters.
    3. Password consisting of letters, digits, and special characters.
    4. Password consisting only of special characters.
    5. Create a password recommended by the author.""")
        choice = int(input("Enter your choice: "))
        Main_menu(choice)

    except ValueError as e:
        print(f"Ошибка: {e}. Пожалуйста, введите положительное целое число для длины пароля.")
    except Exception as e:
        print(f"Произошла ошибка: {e}. Пожалуйста, попробуйте еще раз.")
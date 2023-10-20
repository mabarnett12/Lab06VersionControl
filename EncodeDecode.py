#COP3502C Lab 6
#Margaret Barnett


def encode(input_str):
    new_str = ""

    try:
        for i in range(len(input_str)):
            new_str += str((int(input_str[i]) + 3) % 10)
    except:
        raise ValueError("Invalid input, Non-integer found in password.")

    return new_str


#add decode function here


def get_menu_option():
    print('Menu')
    print('-' * 13)
    print('1. Encode')
    print('2. Decode')
    print('3. Quit\n')
    user_option = int(input('Please enter an option: '))

    if not (1 <= user_option <= 3):
       raise ValueError("Invalid Menu Selection")

    return user_option


def main():
    input_pw = " "

    try:
        menu_option = get_menu_option()
        while menu_option != 3:

            if menu_option == 1:
                input_pw = input('Please enter your password to encode: ')
                encoded_pw = encode(input_pw)
                print('Your password has been encoded and stored!\n')


            elif menu_option == 2:
                if input_pw == " ":
                    raise ValueError('Password to encode not yet entered.')
                decoded_pw = decode(encoded_pw)
                print(f'The encoded password is {encoded_pw}, and the original password is {decoded_pw}.\n')

            menu_option = get_menu_option()

    except ValueError as excpt:
        print(excpt)
        print('Unable to complete request. Please check input and rerun program.')

    except:
        print('Unable to complete request. Please check input and rerun program.')

if __name__ == '__main__':
    main()



#COP3502C Lab 6
#Margaret Barnett


def encode(input_str):
    """Function to encode user input password by adding 3 to each digit of password.
       Included exception handling for non-integer in user input string."""
    new_str = ""

    try:
        for i in range(len(input_str)):
            new_str += str((int(input_str[i]) + 3) % 10)
    except:
        raise ValueError("Invalid input, Non-integer found in password.")

    return new_str


#add decode function here, decode fucntion written, tested, and then removed for partner to add


def get_menu_option():
    """Print user menu and get user menu selection.
       Included exception handling for invalid menu option selection of non-integer or outside of 1-3."""
    print('Menu')
    print('-' * 13)
    print('1. Encode')
    print('2. Decode')
    print('3. Quit\n')

    try:
        user_option = int(input('Please enter an option: '))
    except:
        raise ValueError("Invalid Menu Selection")

    if not (1 <= user_option <= 3):
       raise ValueError("Invalid Menu Selection")

    return user_option


def main():
    input_pw = " "

    try:
        menu_option = get_menu_option()
        while menu_option != 3:

            if menu_option == 1:
                #get and encode user input password
                input_pw = input('Please enter your password to encode: ')
                encoded_pw = encode(input_pw)
                print('Your password has been encoded and stored!\n')


            elif menu_option == 2:
                #decode encoded password back to original user entry and print both
                #exception handling included if user has not yet input a password to encode
                #but selects menu option 2 to decode

                if input_pw == " ":
                    raise ValueError('Password to encode not yet entered.')
                decoded_pw = decode(encoded_pw)
                print(f'The encoded password is {encoded_pw}, and the original password is {decoded_pw}.\n')

            menu_option = get_menu_option()

    #exception handling for various invald user entries in both functions and main
    except ValueError as excpt:
        print(excpt)
        print('Unable to complete request. Please check input and rerun program.')

    except:
        print('Unable to complete request. Please check input and rerun program.')

if __name__ == '__main__':
    main()



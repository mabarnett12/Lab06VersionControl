def decode(input_str):
    new_str = ""

    for i in range(len(input_str)):
        new_str += str((int(input_str[i]) - 3) % 10)

    return new_str
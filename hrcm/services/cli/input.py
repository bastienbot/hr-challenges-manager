def display_and_confirm(message):
    print(message)
    while True:
        user_input = input("Is this correct ?    (Y/N)")
        if user_input in ["y", "Y", "n", "N"]:
            break
        print('Your choice must be either "Y" or "N"')
    return user_input.upper()

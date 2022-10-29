
user_letter = input("Enter a letter: ")
format_letter = user_letter.lower()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

if format_letter in alphabet:
    order = alphabet.index(format_letter) + 1
    if order == 1:
        indicator = 'st'
    elif order == 2:
        indicator = "nd"
    elif order == 3:
        indicator = "rd"
    else:
        indicator = 'th'
    print(f"{user_letter} = {order}{indicator}")

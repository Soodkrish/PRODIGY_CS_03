
def p_strength(password):
    length = len(password)
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)

    strength = 0
    if length >= 16:
        strength += 1
    if has_uppercase :
        strength += 1
    if has_lowercase:
        strength += 1
    if has_digit:
        strength += 1
    if has_special:
        strength += 1
    return strength


def strength(password):

    strength = p_strength(password)

    if  strength == 5:
        print(" \033[1;32;40m |||| Password Has Strong Strength ||||\033[m ")
    elif  strength >= 3:
        print(" \033[1;36;40m ||| Password Has Medium Strength |||\033[m")
    else:
        print(" \033[1;31;40m | !! Password Has Weak Strength !! | \033[m")


password = input("Enter The Password (Min. 4 Characters & Max. 32 Characters) : ")
print()
if len(password) > 32 or len(password) < 4:
    print("\033[1;31;40m **** Password Must Be in Range of 4 to 32 characters ****\033[m\t")
else:
    print(f" Password Length : \033[1;35;40m{len(password)}\033[m")
    print()
    strength(password)

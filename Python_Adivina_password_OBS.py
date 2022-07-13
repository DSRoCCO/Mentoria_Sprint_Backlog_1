

def password():
    intentos = 3

    while intentos > 0:
        intentos -= 1
        word = input("Ingrese Password: ")
        if word =="python3":
            print("Password is Valid")
            break
        else:
            print("Only have left " + str(intentos))
            if intentos == 0:
                print("Password is Invalid")


if __name__ == '__main__':
    password()










def password():
    intentos = 3

    while intentos > 0:
        word = input("Ingrese Password: ")
        intentos -= 1

        if word == "python3":
            print("Password is Valid")
            break
        elif intentos == 0:
            print("Password is Invalid")
            break
        else:
            menssage = "Only have left " + str(intentos)
        print(menssage)




if __name__ == '__main__':
    password()








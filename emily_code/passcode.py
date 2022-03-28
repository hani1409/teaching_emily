import time

def main():
    while True:

        encode = input("Would you like to encode a message (y/n)?")

        encode = encode.lower()

        if encode == 'y':
            encode = True
        elif encode == 'n':
            encode = False
        else:
            break

        text = input("What is your message: ")





        myKey = {'a': 'b',
                 'b': 'c',
                 'c': 'd',
                 'd': 'e',
                 'e': 'f',
                 'f': 'g',
                 'g': 'h',
                 'h': 'i',
                 'i': 'j',
                 'j': 'k',
                 'k': 'l',
                 'l': 'm',
                 'm': 'n',
                 'n': 'o',
                 'o': 'p',
                 'p': 'q',
                 'q': 'r',
                 'r': 's',
                 's': 't',
                 't': 'u',
                 'u': 'v',
                 'v': 'w',
                 'w': 'x',
                 'x': 'y',
                 'y': 'z',
                 'z': 'a'}

        myMessage = ""

        if encode:
            for myChar in text:
                secretChar = myKey.get(myChar.lower(), myChar)
                if not myChar.islower():
                    secretChar = secretChar.capitalize()
                myMessage += secretChar
        else:
            for myChar in text:
                found = False
                for k, v in myKey.items():
                    if myChar.lower() == v:
                        if not myChar.islower():
                            myMessage += k.capitalize()
                            found = True
                        else:
                            myMessage += k
                            found = True
                if not found:
                    myMessage += myChar

        print(myMessage)













if __name__ == '__main__':
    main()

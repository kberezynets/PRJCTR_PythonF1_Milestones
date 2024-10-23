# Alice and Bob are bored during their classes and they want
# to exchange messages for fun.
# To avoid the situation when the teachers catch them and read their notes,
# they agreed to encrypt their messages using the Caesar cipher.

# To make it more secure, they will use a new key every day, so they need help
# to automatically encrypt
# and decrypt messages. They ask for your help.
# Create two Python files encrypt.py and decrypt.py, which will read the user
# message and the key and will output the results.

# Note: only letters get shifted with the preservation of case
# (e.g., T->U and t->u), while punctuation symbols stay the same.

# Enter key: 1
# Enter message: Uif rvjdl cspxo gpy kvnqt pwfs uif mbaz eph.

# Result: The quick brown fox jumps over the lazy dog.

def decrypt(key: int, message: str):
    decrypted = ''
    for char in message:
        if ord(char) in range(97, 123):
            if (ord(char) - key) < 97:
                decrypted += chr((ord(char) - key) + 26)
            else:
                decrypted += chr((ord(char) - key))
        elif ord(char) in range(65, 91):
            if (ord(char) - key) < 65:
                decrypted += chr((ord(char) - key) + 26)
            else:
                decrypted += chr((ord(char) - key))
        else:
            decrypted += char

    print(decrypted)


isInteger = False

while not isInteger:
    key = input('Enter key:')
    isInteger = True
    try:
        check = int(key)
    except ValueError:
        isInteger = False
        print("That's not an integer!")


message = input('Enter message:')

decrypt(int(key), message)

# decrypt(1, 'Uif rvjdl cspxo gpy kvnqt pwfs uif mbaz eph.')

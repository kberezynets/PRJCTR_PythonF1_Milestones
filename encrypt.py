# Alice and Bob are bored during their classes and they want
# to exchange messages for fun.
# To avoid the situation when the teachers catch them and read their notes,
# they agreed to encrypt their messages using the Caesar cipher.

# To make it more secure, they will use a new key every day,
# so they need help to automatically encrypt
# and decrypt messages. They ask for your help.
# Create two Python files encrypt.py and decrypt.py, which will read the user
# message and the key and will output the results.

# Note: only letters get shifted with the preservation of case
# (e.g., T->U and t->u), while punctuation symbols stay the same.

# Enter key: 1
# Enter message: The quick brown fox jumps over the lazy dog.

# Result: Uif rvjdl cspxo gpy kvnqt pwfs uif mbaz eph.

def encrypt(key: int, message: str):
    encrypted = ''
    for char in message:
        if ord(char) in range(97, 123):
            if (ord(char) + key) > 122:
                encrypted += chr((ord(char) + key) - 26)
            else:
                encrypted += chr(ord(char) + key)
        elif ord(char) in range(65, 91):
            if (ord(char) + key) > 90:
                encrypted += chr((ord(char) + key) - 26)
            else:
                encrypted += chr(ord(char) + key)
        else:
            encrypted += char

    print(encrypted)


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

encrypt(int(key), message)

# encrypt(1, 'The quick brown fox jumps over the lazy dog.')

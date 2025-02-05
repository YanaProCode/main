"""
OT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
"""

def rot13(message):
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    alphabet_higher = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encoded_message = ''
    for letter in message:
        if letter in alphabet_lower:
            index = alphabet_lower.index(letter)
            encoded_message += alphabet_lower[index + 13]
        elif letter in alphabet_higher:
            index = alphabet_higher.index(letter)
            encoded_message += alphabet_higher[index+13]
        else:
            encoded_message += letter
    return encoded_message

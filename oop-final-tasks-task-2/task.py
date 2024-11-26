class Cipher:

    def __init__(self, keyword):
        self.keyword = keyword
        self.alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
        alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.cipher = ""
        for letter in self.keyword.lower() + alphabet_lower:
            if letter not in self.cipher:
                self.cipher += letter
        for letter in self.keyword.upper() + alphabet_upper:
            if letter not in self.cipher:
                self.cipher += letter

    def encode(self, data):
        self.data = data
        encoded_data = ""
        positions_list = []  # list with positions of needed letters in the alphabet
        for letter in self.data:
            if letter == " ":
                positions_list.append(555)  # appending some number to identify it as space
            else:
                position = self.alphabet.find(letter)
                positions_list.append(position)
        for position in positions_list:
            if position == 555:
                encoded_data += " "
            else:
                encoded_data += self.cipher[position]
        return encoded_data

    def decode(self, data):
        self.data = data
        decoded_data = ""
        positions_list = []  # list with positions of needed letters in the alphabet
        for letter in self.data:
            if letter == " ":
                positions_list.append(555)  # appending some number to identify it as space
            else:
                position = self.cipher.find(letter)
                positions_list.append(position)
        for position in positions_list:
            if position == 555:
                decoded_data += " "
            else:
                decoded_data += self.alphabet[position]
        return decoded_data


cipher = Cipher("crypto")
print(cipher.encode("Hello world"))
print(cipher.decode("Fjedhc dn atidsn"))

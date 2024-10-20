def decode_ASCII(cipher_text):
    cipher_text = input("Enter the cipher string : \n")
    decode_string = bytes.fromhex(cipher_text)
    return decode_string

print(decode_ASCII(cipher_text))



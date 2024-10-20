def decode_ASCIIHEX(cipher_text):
    decode_string = bytes.fromhex(cipher_text)
    return decode_string
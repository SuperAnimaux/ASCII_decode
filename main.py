from ASCII_hex_decode import decode_ASCIIHEX
from ASCII_bin_decode import partitioning_bin


def decode():
    cipher = input("Enter the cipher : \n")

    cipher_type = int(input("Entre the cipher type (Only ASCII):\n\n 1 = Hex\n 2 = Bin\n\n"))
    if cipher_type == 1 :
        result =decode_ASCIIHEX(cipher)
    elif cipher_type == 2:
        part_bin = partitioning_bin(cipher)
        result = ''.join([chr(int(byte, 2)) for byte in part_bin])
    else:
        result = "ERROR : unexpected argument"
    return result

print(decode())

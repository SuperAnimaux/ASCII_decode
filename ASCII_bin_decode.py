def partitioning_bin(cipher_bin):
    partitioned_cipher = []
    for i in range(0, len(cipher_bin), 8):
        partitioned_cipher.append(cipher_bin[i : i + 8])
    return partitioned_cipher

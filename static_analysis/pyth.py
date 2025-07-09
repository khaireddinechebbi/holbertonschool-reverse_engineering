#!/usr/bin/python3

def decrypt_flag(hex_string):
    key = b"mysecretkey"
    key_len = len(key)
    encrypted = bytes.fromhex(hex_string)
    decrypted = bytearray(len(encrypted))

    for i in range(len(encrypted)):
        r = encrypted[i]
        k1 = key[i % key_len]
        k2 = key[(i + 1) % key_len]
        c = (r - k2) & 0xFF  # byte subtraction mod 256
        c = c ^ k1
        decrypted[i] = c

    return decrypted.decode('utf-8')

hex_string = "9E89846A786585866A977D797C8463807C7F6B67848BAB907B698370896B997C797C8D6C6F7E81AE866AB36D7B7F669D7E6A7F96678F9382898263B474"
print(decrypt_flag(hex_string))

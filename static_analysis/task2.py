#!/usr/bin/python3

import struct

# Extracted values
exponent = 0xffffffffffff
modulus = 0xffffffffffffffb

# Encrypted flag bytes (little-endian format)
encrypted_bytes = bytes.fromhex(
    "8e82d972b66c836fa896da60a7779a69"
    "bc84db77a0729877a582d1758c778461"
    "a883da69ba70905fa498c14fba6da861"
    "9980c063a763f700ffffffffffff0000"
)

# Calculate XOR key
key = pow(2, exponent, modulus)

# Convert encrypted bytes to 8-byte chunks (qwords)
chunks = [encrypted_bytes[i:i+8] for i in range(0, len(encrypted_bytes), 8)]

# Decrypt each chunk
flag_bytes = bytearray()
for chunk in chunks:
    # Convert chunk to integer (little-endian)
    encrypted_qword = int.from_bytes(chunk, byteorder='little')
    # XOR with key
    decrypted_qword = encrypted_qword ^ key
    # Convert back to bytes
    flag_bytes.extend(decrypted_qword.to_bytes(8, byteorder='little'))

# Clean up the flag (remove padding and non-printable chars)
try:
    flag = flag_bytes.decode('utf-8').strip('\x00')
    print(f"Decrypted flag: {flag}")
except UnicodeDecodeError:
    # If UTF-8 fails, look for flag pattern
    flag_start = flag_bytes.find(b'HTB{')
    if flag_start >= 0:
        flag_end = flag_bytes.find(b'}', flag_start) + 1
        print(f"Flag found: {flag_bytes[flag_start:flag_end].decode('ascii')}")
    else:
        print("Couldn't decode as UTF-8. Hex dump:")
        print(flag_bytes.hex(' '))
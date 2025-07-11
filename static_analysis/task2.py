#!/usr/bin/python3

# Extracted values
exponent = 0xffffffffffff
modulus = 0xffffffffffffffb

# Encrypted flag bytes
encrypted_bytes = bytes.fromhex(
    "8e82d972b66c836fa896da60a7779a69"
    "bc84db77a0729877a582d1758c778461"
    "a883da69ba70905fa498c14fba6da861"
    "9980c063a763f700ffffffffffff0000"
)

# Calculate XOR key
key = pow(2, exponent, modulus)

# Decrypt and get full flag bytes
flag_bytes = bytes([b for i in range(0, len(encrypted_bytes), 8) 
                   for b in (int.from_bytes(encrypted_bytes[i:i+8], 'little') ^ key).to_bytes(8, 'little')])

# Find the complete flag (from 'Holberton' to '}')
holberton_pos = flag_bytes.find(b'Holberton')
if holberton_pos != -1:
    end_brace = flag_bytes.find(b'}', holberton_pos)
    print(flag_bytes[holberton_pos:end_brace+1].decode())
else:
    # Fallback if structure changes
    print(flag_bytes.decode('ascii', errors='ignore').strip('\x00'))
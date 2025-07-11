#!/usr/bin/python3

obfuscated_flag = [
    0x8a, 0x101, 0x11e, 0x178, 0x163, 0x108, 0x136, 0x101,
    0x104, 0x12d, 0x178, 0x17f, 0x165, 0x11d, 0x171, 0x136,
    0x101, 0x171, 0x17f, 0x135, 0x135, 0x163, 0x11b, 0x178,
    0x11e, 0x127, 0x3f, 0x12b
]
divisor = 3

flag_chars = []

for val in obfuscated_flag:
    val = val ^ 0x55
    val = val - 7
    q, r = divmod(val, divisor)
    # The assembly compares low byte of quotient == low byte of remainder,
    # so for valid input, these must be equal
    # Let's assume the flag is the quotient (q)
    flag_chars.append(q)

# Convert quotients to characters
flag = ''.join(chr(c) for c in flag_chars)
print(flag)

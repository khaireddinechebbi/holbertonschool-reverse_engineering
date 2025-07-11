#!/usr/bin/python3
import string

check_values = [
    0x80, 0xe4, 8, 0x18, 0x4a, 0x58, 0xb8, 0xe4, 0xac, 0x34,
    0x58, 0xe4, 0x7e, 0xbc, 0x9e, 0x8c, 0x7e, 0xd0, 0xc0, 0x7c,
    0xac, 0xf4, 0x7e, 0x28, 0x9e, 4, 0x7e, 0xbc, 0x9e, 0x8c,
    0x7e, 0x5c, 0x14, 0x4c, 0x7e, 0x5c, 0x7e, 0x6c, 2, 0x14,
    0xb8, 0x4c, 0x14, 0xa4, 0x9e, 8, 0x7e, 0xe4, 0xf4, 8,
    0x6a, 0x14, 0xa6, 0x5c, 0xb8, 0x7c, 0x9e, 0x28, 0x3e, 0xac,
]

allowed_chars = string.ascii_letters + "_"  # a-z, A-Z, _
final_chars = "!@#$%^&*()_+{}:\"<>?"

flag = [""] * (60 - 9)

def reverse_even(value):
    for c in allowed_chars:
        res = (ord(c) * -46) ^ -368
        if (res & 0xff) == value:
            return c
    return "?"

def reverse_odd(value):
    for c in allowed_chars:
        res = (ord(c) * 316) ^ 2528
        if (res & 0xff) == value:
            return c
    return ""

def reverse_final(value):
    for c in final_chars:
        res = (ord(c) * -46) ^ -368
        if (res & 0xff) == value:
            return c
    return ""

# Decode from index 9 to 58
for i in range(9, 59):
    val = check_values[i]
    if i % 2 == 0:
        flag[i - 9] = reverse_even(val)
    else:
        flag[i - 9] = reverse_odd(val)

# Final symbol (index 59)
flag[59 - 9] = reverse_final(check_values[59])

print("Holberton{" + "".join(flag) + "}")

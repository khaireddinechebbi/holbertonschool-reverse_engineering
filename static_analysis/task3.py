#!/usr/bin/python3

check_values = [
    0x80, 0xe4, 8, 0x18, 0x4a, 0x58, 0xb8, 0xe4, 0xac, 0x34,
    0x58, 0xe4, 0x7e, 0xbc, 0x9e, 0x8c, 0x7e, 0xd0, 0xc0, 0x7c,
    0xac, 0xf4, 0x7e, 0x28, 0x9e, 4, 0x7e, 0xbc, 0x9e, 0x8c,
    0x7e, 0x5c, 0x14, 0x4c, 0x7e, 0x5c, 0x7e, 0x6c, 2, 0x14,
    0xb8, 0x4c, 0x14, 0xa4, 0x9e, 8, 0x7e, 0xe4, 0xf4, 8,
    0x6a, 0x14, 0xa6, 0x5c, 0xb8, 0x7c, 0x9e, 0x28, 0x3e, 0xac,
]

allowed_chars = "abcdefghijklmnopqrstuvwxyz_"
final_chars = "!@#$%^&*()_+{}:\"<>?"

flag = [""] * 60

def reverse_even(index, value):
    for c in allowed_chars:
        res = (ord(c) * -46) ^ -368
        if (res & 0xff) == value:
            return c
    return "?"

def reverse_odd(index, value):
    for c in allowed_chars:
        res = (ord(c) * 316) ^ 2528
        if (res & 0xff) == value:
            return c
    return "?"

for i in range(59):  # skip the last character for now
    val = check_values[i]
    if i % 2 == 0:
        flag[i] = reverse_even(i, val)
    else:
        flag[i] = reverse_odd(i, val)

# Final character (symbol) bruteforce
for sym in final_chars:
    if ((ord(sym) * -46) ^ -368) & 0xff == check_values[59]:
        flag[59] = sym
        break

print("Holberton{" + "".join(flag) + "}")

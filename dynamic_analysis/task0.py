#!/usr/bin/python3

from z3 import *
import time

def solve_flag():
    print("Starting optimized solver...")
    start_time = time.time()
    
    s = Solver()
    flag_chars = [BitVec(f'c_{i}', 8) for i in range(24)]
    
    # Initialize variables
    var_4ch = BitVecVal(0, 32)
    var_48h = BitVecVal(1, 32)
    var_44h = BitVecVal(0, 32)
    var_40h = BitVecVal(1, 32)
    
    # Add realistic constraints (alphanumeric + underscore/hyphen only)
    for c in flag_chars:
        s.add(Or(
            And(c >= 0x30, c <= 0x39),  # 0-9
            And(c >= 0x41, c <= 0x5A),  # A-Z
            And(c >= 0x61, c <= 0x7A),  # a-z
            c == 0x5F,                   # _
            c == 0x2D                    # -
        ))
    
    # Prevent braces in middle part
    for c in flag_chars:
        s.add(c != 0x7D)  # }
        s.add(c != 0x7B)  # {
    
    for i in range(24):
        c = ZeroExt(24, flag_chars[i])
        
        # Calculations with proper bit widths
        term1 = ((i + 1) * c * (i + 2)) & 0xFF
        var_4ch += term1
        
        term2 = ((7 * i) + c + 0x1f) % 0x7b
        var_48h *= term2
        
        term3 = ((i + 1) * c + (i * i)) & 0x1FF
        var_44h += term3
        
        term4 = ((i + 3) * c + 0x11) & 0x3FF
        var_40h ^= term4
    
    # Final checks
    final1 = var_4ch * var_48h
    final2 = final1 + var_44h - var_40h
    final3 = final2 ^ 0xdeadbeef
    final3 = final3 & 0xffffff
    
    final4 = final1 + final3 - (var_44h * var_40h)
    final4 = final4 - 0x35014542
    
    s.add(final4 % 0xf1206 == 0xae44)
    
    # Set timeout (30 minutes)
    s.set("timeout", 1800000)
    
    print("Solving... (may take several minutes)")
    result = s.check()
    
    if result == sat:
        model = s.model()
        middle = ''.join([chr(model.eval(c).as_long()) for c in flag_chars])
        print(f"Solved in {time.time()-start_time:.2f} seconds")
        return f"Holberton{{{middle}}}"
    else:
        return f"No solution found ({result})"

print(solve_flag())
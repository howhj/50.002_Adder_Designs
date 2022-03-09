# To automate the writing of the .bc script

# CARRY LOOKAHEAD ADDER

for i in range(0,32): 
    line1 = f"T{i} := !(!(!(A{i} & B{i}) & A{i}) & !(!(A{i} & B{i}) & B{i}));\n"
    line2 = f"S{i} := !(!(!(T{i} & C{i}) & T{i}) & !(!(T{i} & C{i}) & C{i}));\n"
    line3 = f"P{i} := !(A{i} | B{i});\n"
    line4 = f"G{i} := !(A{i} & B{i});\n"
    print(line1 + line2 + line3 + line4)

print("\n")

for i in range(0,16):
    line1 = f"PA{i} := !(P{i*2+1} | P{i*2});\n"
    line2 = f"GA{i} := !(!(!P{i*2+1} & !G{i*2}) & G{i*2+1});\n"
    line3 = f"C{i*2+1} := !(!(!P{i*2} & CA{i}) & G{i*2});\n"
    line4 = f"C{i*2} := CA{i};\n"
    print(line1 + line2 + line3 + line4)

print("\n")

for i in range(0,8):
    line1 = f"PB{i} := !(PA{i*2+1} & PA{i*2});\n"
    line2 = f"GB{i} := !!(!(GA{i*2} & PA{i*2+1}) & !GA{i*2+1});\n"
    line3 = f"CA{i*2+1} := !(!(PA{i*2} & CB{i}) & !GA{i*2});\n"
    line4 = f"CA{i*2} := CB{i};\n"
    print(line1 + line2 + line3 + line4)

print("\n")

for i in range(0,4):
    line1 = f"PC{i} := !(PB{i*2+1} | PB{i*2});\n"
    line2 = f"GC{i} := !(!(!PB{i*2+1} & !GB{i*2}) & GB{i*2+1});\n"
    line3 = f"CB{i*2+1} := !(!(!PB{i*2} & CC{i}) & GB{i*2});\n"
    line4 = f"CB{i*2} := CC{i};\n"
    print(line1 + line2 + line3 + line4)

print("\n")

for i in range(0,2):
    line1 = f"PD{i} := !(PC{i*2+1} & PC{i*2});\n"
    line2 = f"GD{i} := !!(!(GC{i*2} & PC{i*2+1}) & !GC{i*2+1});\n"
    line3 = f"CC{i*2+1} := !(!(PC{i*2} & CD{i}) & !GC{i*2});\n"
    line4 = f"CC{i*2} := CD{i};\n"
    print(line1 + line2 + line3 + line4)

print("\n")

line1 = "PE0 := !(PD1 | PD0);\n"
line2 = "GE0 := !(!(!PD1 & !GD0) & GD1);\n"
line3 = "CD1 := !(!(!PD0 & OP) & GD0);\n"
line4 = "CD0 := OP;\n"
print(line1 + line2 + line3 + line4)

print("\n")

#=============================================================================

# ORIGINAL ADDER

for i in range(0,32):
    line1 = f"X{i} := A{i} ^ B{i};\n"
    line2 = f"FA_S{i} := X{i} ^ FA_C{i};\n"
    line3 = f"Y{i} := A{i} & B{i};\n"
    line4 = f"Z{i} := X{i} & FA_C{i};\n"
    line5 = f"FA_C{i+1} := Y{i} | Z{i};\n"
    print(line1 + line2 + line3 + line4 + line5)

for i in range(0,32):
    line = f"B{i} := !(!(!(Bx{i} & OP) & Bx{i}) & !(!(Bx{i} & OP) & OP));"
    print(line)
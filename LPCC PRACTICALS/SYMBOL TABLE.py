import os
LC = 0  
mnemonics = {
    'STOP': ('00', 'IS', 0),
    'ADD': ('01', 'IS', 2),
    'SUB': ('02', 'IS', 2),
    'MUL': ('03', 'IS', 2),
    'MOVER': ('04', 'IS', 2),
    'MOVEM': ('05', 'IS', 2),
    'COMP': ('06', 'IS', 2),
    'BC': ('07', 'IS', 2),
    'DIV': ('08', 'IS', 2),
    'READ': ('09', 'IS', 1),
    'PRINT': ('10', 'IS', 1),
    'LTORG': ('05', 'AD', 0),
    'ORIGIN': ('03', 'AD', 1),
    'START': ('01', 'AD', 1),
    'EQU': ('04', 'AD', 2),
    'DS': ('01', 'DL', 1),
    'DC': ('02', 'DL', 1),
    'END': ('AD', 0)
}
REG = {'AREG': 1, 'BREG': 2, 'CREG': 3, 'DREG': 4}
symtab = {}   
symindex = 0
def detect_mn(k):
    global words, LC, symtab, symindex
    mnemonic = words[k]

    if mnemonic == "START":
        LC = int(words[1])
    elif mnemonic == "END":
        pass
    elif mnemonic == "LTORG":
        pass
    elif mnemonic == "ORIGIN":
        LC = int(words[k + 1])
    elif mnemonic == "DS":
        LC += int(words[k + 1])
    elif mnemonic == "DC":
        LC += 1
    else:
        LC += 1
def symbol():
    print("Symbol Table:")
    for key, value in symtab.items():
        print(f"{key}\t{value[0]}\t{value[1]}")
file = open(r"C:\Users\Lenovo\Desktop\STUDY\SEMESTER 6\LPCC\PRACTICAL EXAM\INPUT CODE 1.txt")
for line in file:
    words = line.split()
    k = 0
    if words[0] in mnemonics:
        detect_mn(k)
    else:
        if words[k] not in symtab:
            symtab[words[k]] = (LC, symindex)
            symindex += 1
        else:
            x = symtab[words[k]]
            if x[0] == "**":
                symtab[words[k]] = (LC, x[1])
        k = 1
        detect_mn(k)
symbol()

file.close()

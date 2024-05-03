#use python3 pyunzip.py KSK.zip
#!/usr/bin/env python3

#lex test.l
#gcc lex.yy.c
#./a.out

#lex test.l
#bison -dy test.y
#gcc lex.yy.c y.tab.c -lm
#./a.out

import sys
from zipfile import PyZipFile
for zip_file in sys.argv[1:]:
    pzf = PyZipFile(zip_file)
    pzf.extractall()

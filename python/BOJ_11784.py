import sys
s = sys.stdin.read()
l = s.split("\n")
l.remove("")
for i in l:
    print(bytearray.fromhex(i).decode())

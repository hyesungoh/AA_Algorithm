l = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']
s = []
for w in input():
    if w not in l:
        s.append(w)
print(''.join(s))

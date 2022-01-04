from z3 import *

# List of BitVec
password = [BitVec(f'{i}', 8) for i in range(0x13)]

s = Solver()

for i in range(8,0x11):
    s.add(password[i] == ord('i'))
    


s.add(password[2] == ord('n'))
s.add(password[0] == ord('c'))
s.add(password[1] == ord('a'))
s.add(password[3] == ord('t'))


s.add(password[4] == ord('s'))
s.add(password[5] == ord('p'))
s.add(password[6] == ord('m'))
s.add(password[7] == ord('n'))

s.add(password[17] == ord('u'))
s.add(password[18] == ord('r'))

print(s.check())
model = s.model()
flag = ''.join([chr(int(str(model[password[i]]))) for i in range(len(model))])

print(flag)

[0x42,0x43,0x4d,0x4e,0x50,0x4f]
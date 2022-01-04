from pwn import *
from base64 import * 
byte = []
key = []

data = open('ch30.bin', 'rb').read()
with open('asm.txt', 'w') as f:
    f.write(disasm(data[0xAC5:0x3ec2b5])) #Disasm from begin to end of check()
    f.close()
    
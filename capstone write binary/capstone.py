from pwn import *
from base64 import * 
from capstone import *
byte = []
key = []

data = open('flag.exe', 'rb').read()
md = Cs(CS_ARCH_X86, CS_MODE_64)

with open('asm1.txt', 'w') as f:
    for i in md.disasm(data[0x914:0x85fd], 0x00401514): #Capstone read from data address, not the virtual address
        f.write(f"0x{i.address}:\t{i.mnemonic}\t{i.op_str}\n")
    f.close()
 
status = True   
with open('asm1.txt',"r") as f:
    for line in f.readlines():
        if(line.find("mov	dword ptr [rbp - 0x10]") != -1):
            if(status):
                key.append(0x0)
            pos = line.find(',')
            item = line[pos+1:-1]
            byte.append(int(item,16))
            status = True
       
        elif (line.find('xor') != -1):
            pos = line.find(',')
            item = line[pos+1:-1]
            key.append(int(item,16))
            status = False
            
flag = ""

for i in range(len(byte)):
    flag += chr(key[i+1]^byte[i])

print(flag)

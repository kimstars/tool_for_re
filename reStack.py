import sys

def toHex(a):
    try:
        for inp in a:
            res = []
            if(len(inp) % 2 != 0):
                print("Hãy điền chuỗi chẵn kí tự!!") 
            else:
                for i in range(len(inp)//2):
                    t = "0x"
                    t += (inp[i*2:i*2+2]) +","
                    res.append(t)
                res = res[::-1]
                res = "".join(res)
            print(res, end="")
    except:
        pass
        
print(" _____________________________")
print("|Tool đảo cắt xâu hex địa chỉ |")
print("|         CTK                 |")
print("|123456 -> \\x56\\x34\\x12       |")
print("|_____________________________|")


a = ["2591B915", "D5F7BF06", "7B55A62F", "0AB47E66", "76CC59A1", "5DCE003B", "A5D41B3A", "5BBB44EA", "C90D0B04", "E16EB66A", "078B" ] 


b = ["05F4D161","BB9EDE76","0F30CA0F","65CD5E15","18A779D4","24EE7754","C4F46E55","289B2198","A5616270","8802D74A","62FD" ]

c = ["22463415","CE8CD902","704B2CBA","466F715A","632C480F"]

d = ["05F4D161","BB9EDE76","0F30CA0F","65CD5E15","18A779D4","24EE7754","C4F46E55","289B2198","A5616270","8802D74A"]
toHex(d)



import sys

def toHex():
    
    print("Nhập địa chỉ :")
    # inp = sys.argv[1]
    inp = input()
    try:
        if(len(inp) % 2 != 0):
            print("Hãy điền chuỗi chẵn kí tự!!") 
        else:
            res = []
            for i in range(len(inp)//2):
                t = "\\x"
                t += (inp[i*2:i*2+2])
                res.append(t)
            res = res[::-1]
            res = "".join(res)
            print("KẾT QUẢ ^^ :")
            print(res)
    except:
        pass
        
print(" _____________________________")
print("|Tool đảo cắt xâu hex địa chỉ |")
print("|         CTK                 |")
print("|123456 -> \\x56\\x34\\x12       |")
print("|_____________________________|")

toHex()



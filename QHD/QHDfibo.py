
fibo = {0:0,1:1}


def roll(i):
    if(i not in fibo):
        val = roll(i-1) +roll(i-2)
        fibo[i]  = val
    return fibo[i]

print(roll(31))
# print(fibo)
        

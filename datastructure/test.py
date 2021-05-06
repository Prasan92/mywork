def weighted_char(w):
    s=""
    d={"A":1}
    for i in range(2,27):
        a=i+64
        d[chr(a)]=i*d[chr(a-1)]+d[chr(a-1)]
        print(d[chr(a)])
    for i in range(26,0,-1):
        char=chr(i+64)
        if d[char] > w:
            continue
        else:
            divisor=w//d[char]
            s=divisor*char+s
            w-=divisor*d[char]
    return s


ret=weighted_char(65)
print(ret)

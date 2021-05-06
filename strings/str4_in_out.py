# Program for the requirement,input: a4k3b2 and expected output: aeknbd

s='a4k3b2'
prev = s[0]
i=0
out=''

for ch in s:
    if ch.isalpha():
        out=out+ch
        x=ch
    else:
        d=int(ch)
        new=chr(ord(x)+d)
        out=out+new
        print(out)

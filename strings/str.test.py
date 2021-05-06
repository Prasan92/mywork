

s='aaaabbbccz'
output=''
c=1
i=1
prev=s[0]
while i<len(s):
    if s[i] == prev:
        c=c+1
    else:
        output=output+str(c)+prev
        prev = s[i]
        c=1
    if i == len(s)-1:
        output=output+str(c)+prev
        i=i+1
        print(output)
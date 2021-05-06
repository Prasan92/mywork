#Program for the requirement,input: aaaabbbccz and expected output: 4a3b2c1z:

s='aaaabbbccz'
prev = s[0]
output = ''
c = 1
i = 1
while i<len(s):
    if s[i] == prev:
        c = c + 1
    else:
        output = output + str(c)+prev
        prev = s[i]
        c = 1
    if i == len(s)-1 :
        output = output + str(c)+prev
        i = i + 1
    print(output)


    

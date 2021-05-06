#merge characters of 2 strings into a single string by taking characters alternatively:

s1 = input('enter first string: ')
s2 = input('enter seconf string: ')
i,j = 0,0
output = ''
while i<len(s1) or j<len(s2):
    if i<len(s1):
        output = output + s1[i]
        i = i + 1
    if j<len(s2):
        output = output + s2[j]
        j = j + 1
    print(output)




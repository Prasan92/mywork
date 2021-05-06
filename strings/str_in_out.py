# Program for the requirement,input: a4b3c2 and expected output: aaaabbbcc:


s = input('enter the string: ')
output = ''
for ch in s:
    if ch.isalpha():
        x = ch
    else:
        d = int(ch)
        output = output + x * d
    print(output)

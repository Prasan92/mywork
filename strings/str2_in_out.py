#. Program for the requirement,input: a3z2b4 and expected output: aaabbbbzz (sorted String):

s='a3z2b4'
output = ''

for ch in s:
    if ch.isalpha():
        x = ch
    else:
        d = int(ch)
        output = output + x * d
    print(''.join(sorted(output)))

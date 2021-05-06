# sort characters of the string, first alphabet symbols followed by digits:

s = input('enter the alphanumeric string: ')
alpha = []
digit = []
for ch in s:
    if ch.isalpha():
        alpha.append(ch)
    else:
        digit.append(ch)
    print(''.join(sorted(alpha)+sorted(digit)))

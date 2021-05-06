#Program to find the number of occurrences of each character present in the given string with count() method

s='aabbbcccd'
l=[]
for ch in s:
    if ch not in l:
        l.append(ch)
for ch in l:
    print('{} occurs {} no. of times'.format(ch,s.count(ch)))
######

def func():
    s='aabbbccccd'
    d={}
    for i in s:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    print(d)

func()

####

s='aabbccd'
s1=set(s)
for ch in sorted(s1):
    print('{} occurs {} times'.format(ch,s.count(ch)))
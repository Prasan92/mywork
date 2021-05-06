




"""
# Program for the requirement,input: a4b3c2 and expected output: aaaabbbcc:
s = 'a4b3c2'
st=" "
for ch in s:
    if ch.isalpha():
        x = ch
    else:
        st=st+x*int(ch)

print(st)
"""
"""
#sort characters of the string, first alphabet symbols followed by digits:
s = input('enter the string: ')
alpha = []
digit = []
for ch in s:
    if ch.isalpha():
        alpha.append(ch)
    else:
        digit.append(ch)
    print(''.join(sorted(alpha)+sorted(digit)))
"""

"""
#merge characters of 2 strings into a single string by taking characters alternatively
s1 = input("enter string: ")
s2 = input("enter string: ")
s=" "
i=0
j=0
while i<len(s1) or j<len(s2):
    if i<len(s1):
        s=s+s1[i]
    if i<len(s2):
        s=s+s2[i]
    i+=1
    j+=1
print(s)
"""

"""s = input('enter the string: ')
i=0
while i<len(s):
    print(s[i])
    i=i+2
"""

"""
##REVERSE internal content of every second word present in the given string
st = "one two three four five six"
splt = st.split(" ")
l=[]
i=0
while i<len(splt):
    if i%2 == 0:
        l.append(splt[i])
    else:
        l.append(splt[i][::-1])
    i+=1
print(l)

"""

"""#reverse internal content of each word:
st="just fucking do it"
l=st.split(" ")
lis=[]
for i in l:
    lis.append(i[::-1])
    s=" ".join(lis)

print(s)
"""

"""# reverse order of words in given string:
st = "just fucking do it"

l=st.split(" ")
s=" ".join(l[::-1])
print(s)"""


"""s="prasanna"

i = len(s)-1
st=" "
while i >=0:
    st=st+s[i]
    i= i-1

print(st)"""

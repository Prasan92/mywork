
"""
#Program for the requirement,input: aaaabbbccz and expected output: 4a3b2c1z:
s = "aaaabbbccz"
d={}

def fun():
    for i in s:
        if i not in d:
            d[i] = [i]
        else:
            d[i].append(i)
    #print(d)
    l = []
    for k, v in d.items():
        c = len(v)
        l.append(str(c) + k)
        out = "".join(l)
    return out
"""
#-------------------
"""
def compress(s):
    #aaaabbbccz
    out=''
    count=1
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            count+=1
        else:
            out+=s[i-1]+str(count)
            count=1
    out+=s[i-1]+str(count)
    print(out)
compress("aaaabbbccz")
"""
"""
def compress2(s):
    out=''
    count=1
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            count+=1
        else:
            out+=s[i]+str(count)
            count=1
    out+=s[i]+str(count)
    print(out)

#------------
def findsubtr(s,p):
    for i in range(len(s)-1):
        if p == s[i:len(p)+i]:
            return True,s[i:len(p)+i]
    return False,None
"""
#---------------------------------------------------------------
"""
# Program for the requirement,input: a4b3c2 and expected output: aaaabbbcc:
s = 'a4b3c2'
output = ''
for ch in s:
    if ch.isalpha():
        x = ch
    else:
        output = output + x * int(ch)
    print(output)
"""
"""
# sort characters of the string, first alphabet symbols followed by digits:
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
"""
"""
s = input('enter the string: ')
print('print char in even index')
i=0
while i<len(s):
    print(s[i])
    i=i+2
print('enter char in odd index')
i=1
while i<len(s):
    print(s[i])
    i=i+2
print('char in odd index')
"""
"""
#reverse every second word of the sentence
s="one two three four five six"
l=[]
ts = s.split(" ")
print(ts)
i=0
while i<len(ts):
    if i%2 == 0:
        l.append(ts[i])
    else:
        l.append(ts[i][::-1])
    i+=1
    out=" ".join(l)
print(out)
"""
"""
#reverse each word in a sentence
s="just fucking do it"
l=[]
for word in s.split(" "):
    l.append(word[::-1])
    output = " ".join(l)
print(output)
"""
"""
lis=[4,1,2,3,2,1,3,1,2,3]
d={}
for i in lis:
    if i not in d.keys():
        d[i]=[]
    else:
        d[i].append(i)

for j in d.values():
    for k in j:
        print(k)

print(d)"""
#-----------------------------------
"""class fun():
    def __init__(self,filename,mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename,self.mode)
        return self.file

    def __exit__(self,type,val,traceback):
        self.file.close()"""


"""with open("sample.txt","r") as f:
    print(f.read())

print(f.closed)"""
#----------------------------------------------------------------------

"""
lambda and function 
l=[1,2,3,4,5]

#lis=list(map(lambda x: x*x, l))
#print(lis)

def fun(f,arg):
    lis = []
    for i in arg:
        lis.append(f(i))
    return lis

def square(x):
    return x*x

squares=fun(square,l)"""

"""
t=[(1, "gfg"), (1, "is"), (2, "best"), (3, "for"), (4, "CS")]

#{1: [‘gfg’, ‘is’], 2: [‘best’], 3: [‘for’], 4: [‘CS’]

d={}
for i in t:
    if i[0] not in d.keys():
        d[i[0]]=[i[1]]
    else:
        d[i[0]].append(i[1])

print(d)
"""
"""t = [{'gfg' : [1, 5, 6, 7], 'good' : [9, 6, 2, 10], 'CS' : [4, 5, 6]},
    {'gfg' : [5, 6, 7, 8], 'CS' : [5, 7, 10],'best':[]},
    {'gfg' : [7, 5], 'best' : [5, 7]}]

d={}
for i in t:
    for k,v in i.items():
        if k not in d.keys():
            d[k]=[v]
        else:
            d[k].append(v)

d2={k:[j for i in v for j in i] for k,v in d.items() }

print(d2)
"""

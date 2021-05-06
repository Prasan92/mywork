#Program for the requirement,input: ABAABBCA and expected output: 4A3B1C

s='abaabbca'
output=''
d={}
for ch in s:
    if ch not in d:
        d[ch]=1
    else:
        d[ch]+=1
for k,v in sorted(d.items()):
    output=output+str(v)+k
    print(output)

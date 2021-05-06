#REVERSE internal content of every second word present in the given string

st = 'one two three four five six'
ts = st.split()
print(ts)
l = []
i = 0
while i<len(ts):
    if i%2 == 0:
        l.append(ts[i])
    else:
        l.append(ts[i][::-1])
    i = i+1
    out = ' '.join(l)
    print(out)



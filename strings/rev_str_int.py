# reverse internal content of each word:

st = 'just fucking do it'
ts = st.split()
els = []
for word in ts:
    els.append(word[::-1])
    out = ' '.join(els)
    print(out)

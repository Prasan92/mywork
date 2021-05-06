# reverse order of words in given string:

st = 'just fucking do it'
st_split = st.split()
st_rev = st_split[::-1]
ts = ' '.join(st_rev)
print(ts)
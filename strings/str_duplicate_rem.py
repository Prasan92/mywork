# Program for the requirement,input: a4k3b2 and expected output: aeknbd:

s='aaabbbcccddddeee'
l=[]
for ch in s:
    if ch not in l:
        l.append(ch)
        output=''.join(l)
        print(output)


            #for ch in s:
                #if ch not in out:(empty string)
                         # out=out+ch
                         # print(out)

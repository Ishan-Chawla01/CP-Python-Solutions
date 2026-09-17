word="cCceDC"
contenders=[]
repeated=[]
count=0
for w in range(len(word)):
    if word[w].islower():
        contenders.append(word[w])
    if word[w].isupper() and word[w].lower() in contenders and word[w].lower() not in word[w+1:] and word[w].lower() not in repeated:
        print(word[w])
        repeated.append(word[w].lower())
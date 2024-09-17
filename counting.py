
a=["Apple","Apple","Orange"]

count={}

for word in a:
    if word in count:
        count[word]+=1
    else:
        count[word]=1

for x , y in count.items():
    print(x,y)
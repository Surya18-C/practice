
a=[1,3,5,4,2]

largest=a[0]

second=0

for x in a:
    if x > largest:
        second=largest
        largest=x

print(largest)
print(second)
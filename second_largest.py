
numbers=[10,20,30,40,50]

largest=numbers[0]

second=0

for x in numbers:
    if x > largest:
        second=largest
        largest=x

print(largest)

print(second)



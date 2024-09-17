


# n1=int(input("Enter 1st : "))
# n2=int(input("Enter 2nd : "))
#
# def add(a,b):
#     c=a+b
#     print(c)
#
# add(n1,n2)

# x=lambda a,b : a+b
#
# print(x(10,20))

# def add(a,b):
#     c=a+b
#     return c
#
# add(10,20)
#
# v=add(10,20)
# print(v)

# def add(*args):
#     total=0
#
#     for i in args:
#         total+=i
#     return total
#
# print(add(10,20,30,40,50,60,70))


def factorial(n):
    if n==0:
        return 1
    else:
       return n*factorial(n-1)

print(factorial(5))
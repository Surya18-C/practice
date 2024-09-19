

def squre(x):
   if x==1:
      return "sam"
   elif x==2:
      return "Babu"
   else:
      return x


val=[1,2,3,4,5]

a=map(squre , val)

print(set(a))

class A:

    def __init__(self,name,age):
        self.n=name
        self.a=age

    def demo(self):
        print("Hello",self.n,self.a)

obj=A("Rex",20)
obj2=A("Babu",30)

obj.demo()
obj2.demo()

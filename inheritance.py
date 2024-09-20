
"""class father:
    def land(self):
        print("Fathers Land")

class son(father):
    pass

obj=father()

obj.land()"""

#************************* Multi level Inheritance *************

class fater:
    def land(self):
        print("Land")

class mother(fater):
    def jeweler(self):
        print("Jewelery")

class uncle(mother):
    def money(self):
        print("money")

class son(fater,mother):
    pass

obj = mother()

obj.land()
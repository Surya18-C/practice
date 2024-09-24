
# class company:
#
#     def __init__(self):
#
#         self.name="Digibyte"
#
#     def sample(self):
#         print(self.name)
#
#
# obj=company()
#
# obj.name="Amazon"
#
# obj.sample()


#***************************** Private *********
# class company:
#
#     def __init__(self):
#
#         self.__name="Digibyte"
#
#     def sample(self):
#         print(self.__name)
#
#
# obj=company()
#
# obj.__name="Amazon"
#
# obj.sample()


#****************************** Produted ***************

class company:

    def __init__(self):

        self._name="Digibyte"

    def sample(self):
        print(self._name)

class office(company):

    def demo(self):
        print(self._name)


obj=office()

obj.name="Amazon"

obj.demo()
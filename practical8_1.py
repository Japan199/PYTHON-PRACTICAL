class Base1:
    def __init__(self):
        print ("hello")
    def hello(self):
        print ("In Base class one")
class Base2:
    def __init__(self):
        print("hi")
    def hello(self):
        print("In Base class two")
class multiple_inheritance(Base1,Base2):
    pass
r=multiple_inheritance()
r.hello()#MRO
class multiple_inheritance1(Base2,Base1):
    pass
rs=multiple_inheritance1()
rs.hello()#MRO
class circle:
    radius=0
    def __init__(self,r):
        self.radius = r
    def area(self):
        print("Area : ",(3.14*self.radius*self.radius))
    def parameter(self):
        print("Parameter : ",(3.14*self.radius*2))

c1 = circle(1)
c1.area()
c1.parameter()
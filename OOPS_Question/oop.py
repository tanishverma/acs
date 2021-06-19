#Base Class
class X():
    def __init__(self,name):
        self.name = name
    
    def execute(self,dictionary):
        print("Arguments:", dictionary)
        print("Object Name:", self.name)
        print("Class Name:", self.__class__.__name__)

    def shutdown(self):
        print("Object Name:", self.name)
        print("Class Name:", self.__class__.__name__)
        print("Shutdown Called")
        exit()

class A(X):
    pass
class B(X):
    pass
class C(X):
    pass

obj_X = X(11)
obj_X.execute({"X":11})
#obj_X.shutdown()
#Initialising Classes A,B and C
obj_A = A("Class_A")
obj_B = B("Class B")
obj_C = C("Class_C")

obj_A.execute({"A":"Class_A"})
#obj_A.shutdown()

obj_B.execute({"B":0.99})
#obj_B.shutdown()

obj_C.execute({"C":"Class_C"})
obj_C.shutdown()
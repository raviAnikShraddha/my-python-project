class A:
    def state_1(self):
        print("State 1")

    def state_2(self):
        print("State 2")

    def state_3(self):
        print("State 3")

class B(A):
    def state_1(self):
        print("State 1 from child class")

    def state_4(self):
        print("State 4")

    def state_5(self):
        print("State 5")


b = B()
b.state_1()
b.state_2()
b.state_3()
b.state_5()
b.state_4()
'''
a = A()
a.state_1()
a.state_2()
'''
# Multi Level Inheritance
class C(B):
    def state_6(self):
        print("State 6")

c = C()
class Example:
    def __init__(self):
        self.name = 'Narasimha'
        self.section = 'ECE'
        print("my name is {} and I am from {} Background".format(self.name,self.section))

e1 = Example()
e1.name = 'Ravi'
e1.section = 'CSE'
print("my name is {} and I am from {} background".format(e1.name,e1.section))

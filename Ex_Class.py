class Student:
    #per_rise = 1.05
    def __init__(self,first,last,marks):
        self.first = first
        self.last = last
        self.marks = marks
        self.email = first+'.'+last+'@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.marks = int(self.marks*1.05)
        if self.marks > 100:
            self.marks = 100
        else:
            return self.marks

s1 = Student('Narasimha','Gade',99)
s2 = Student('Alex','Parish',98)

print(s1.marks)
s1.apply_raise()


print(s1.marks)

print(s2.marks)
s2.apply_raise()
print(s2.marks)

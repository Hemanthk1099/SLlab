class Student:
    def __init__(self,name=None,age=None,marks=[None]):
        self.name=name
        self.marks=marks
        self.age=age
    def display(self):
        print("\nName:",self.name,"\nAge:",self.age,"\nMARKS")
        for i in range(3):
            print("Subject",i+1,":",self.marks[i])
    def accept(self):
        self.name=input("Enter name:")
        self.age=input("Enter age:")
        self.marks=[]
        for i in range(3):
            print("Subject",i,": ")
            self.marks.append(float(input()))
s1=Student("Peter","17",[45,67,99])
s2=Student("Steve","38",[66,89,100])
s1.display()
s3=Student()
print("Enter details")
s3.accept()
s3.display()

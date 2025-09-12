class student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def display(self):
        print("name of student:",self.name)
        print("rollno of student:",self.rollno)
        print("marks of student:",self.marks)
s1=student("akhil",590,90)
s1.display()
s2=student("ajay",500,80)
s2.display()


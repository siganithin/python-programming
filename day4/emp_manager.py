class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print(f"name:{self.name} \n salary:{self.salary}")
class manager(employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
    def display(self):
        super().display()
        print("department:",self.department)
emp1=employee("ajay",5000)
emp1.display()
mng1=manager("bharath",6000,"cse")
mng1.display()
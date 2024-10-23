

class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def get_info(self):
        print("Full Name:", self.fname, self.lname)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, fname, lname, age, std_id):
        super().__init__(fname, lname, age)
        self.std_id = std_id

    def get_stuinfo(self):
        self.get_info()
        print("StudentID:", self.std_id)


class Employee(Person):
    def __init__(self, fname, lname, age, emp_id, salary):
        super().__init__(fname, lname, age)
        self.emp_id = emp_id
        self.salary = salary

    def get_empinfo(self):
        self.get_info()
        print("Employee no:", self.emp_id + "\nSalary:", self.salary, "USD")


student1 = Student("Anthony", "Smith", 35, "s123456")
student1.get_stuinfo()

print("=" * 20)

emp1 = Employee("Sarah", "Taylor", 34, "2919736", 5000)
emp1.get_empinfo()


class Student():
    passingMark = 50

    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def __str__(self) -> str:
        return f"Name: {self.name}, mark: {self.mark}"

    def passOrFail(self):
        if self.mark >= self.passingMark:
            return "Pass"
        else:
            return "Fail"


# Creating student1 and 2
student1 = Student("John", 52)
student2 = Student("Jenny", 69)

# Checking for passOrFail
status1 = student1.passOrFail()
status2 = student2.passOrFail()

print(student1)
print(status1 + "\n")

print(student2)
print(status2 + "\n")

# Updating the class variable passingMark to 60 and rechecking for passOrFail
Student.passingMark = 60

status1 = student1.passOrFail()
status2 = student2.passOrFail()

print(student1)
print(status1 + "\n")

print(student2)
print(status2 + "\n")

# class student:
#     def __init__(self):
#         self.hello()
#
#     def hello(self):
#         print("Hello")
#
# student()
#
# class student:
#     def __init__(self,sub1,sub2,sub3):
#         self.sub1 = sub1
#         self.sub2 = sub2
#         self.sub3 = sub3
#
#     def average(self):
#         res = (self.sub1+self.sub2+self.sub3)/3
#         print(round(res,2))
#
# user1 = student(75,82,63)
# user1.average()

# class student:
#     def __init__(self,prod1,prod2,prod3):
#         self.prod1 = prod1
#         self.prod2 = prod2
#         self.prod3 = prod3
#
#     def total(self):
#         res = (self.prod1+self.prod2+self.prod3)
#         print("$",res)
#
# customer1 = student(150,400,200)
# customer1.total()

# class student:
#     def __init__(self, prod1: list):
#         self.prod1 = prod1
#
#     def avg(self):
#         print( sum(self.prod1)/len(self.prod1))
#
# customer1 = student([10,56])
# customer1.avg()


class CSE_class:
    def __init__(self, list_of_students):
        self.list_students = list_of_students
        self.class_average = self.total_average()

    def total_average(self):
        total = 0
        for student in self.list_students:
            total += student.percent

        return round((total/len(self.list_students)),2)

class Student:
    def __init__(self, sub1, sub2, sub3):
        self.subj1 = sub1
        self.subj2 = sub2
        self.subj3 = sub3
        self.percent = self.average()

    def average(self):
        res = (self.subj1 + self.subj2 + self.subj3)/300*100
        return round(res, 2)


user1 = Student(80,80, 80)
user2 = Student(75,82, 45)
user3 = Student(75,82, 45)
user4 = Student(75,82, 45)

cse = CSE_class([user3, user2, user1, user4])
print(cse.class_average)
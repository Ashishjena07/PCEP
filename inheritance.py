
class tasks:

    def __init__(self,pro1,pro2,pro3,pro4,pro5):
        self.pro1 = pro1
        self.pro2 = pro2
        self.pro3 = pro3
        self.pro4 = pro4
        self.pro5 = pro5

    def total_price(self):
        data = (self.pro1+self.pro2+self.pro3+self.pro4+self.pro5)*0.18
        data1 = (self.pro1+self.pro2+self.pro3+self.pro4+self.pro5)
        print("Total price: ",data1)
        print("GST amount : ",data)
        print("Finall Billing : ",data1+data)

class person(tasks):

    def __init__(self, name, pro1, pro2, pro3, pro4, pro5):
        super().__init__(pro1, pro2, pro3, pro4, pro5)
        self.name = name

    def display(self):
        print(f"User name : {self.name}")
        print(f"Product1 : {self.pro1}")
        print(f"Product2 : {self.pro2}")
        print(f"Product3 : {self.pro3}")
        print(f"Product4 : {self.pro4}")
        print(f"Product5 : {self.pro5}")





user1 = person("ashish",25,36,54,54,89)
user1.display()
user1.total_price()
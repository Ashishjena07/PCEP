from pymongo import MongoClient
client = MongoClient()
dbname = client["First-Database"]
collection_name = dbname["Student_details"]
class personal:
    def __init__(self):
        self.city = "Rourkela"
        self.state = "Odisha"
        self.pin = "769007"
        self.country = "India"
class student(personal):
    def __init__(self, name, username,**kwargs):
        self.name = name
        self.username = username
        self.personal = vars(personal())
        self.kwargs = kwargs

s1 = student(name="Ashish",
             username="Ashishjena",
             college="GIETU",
             dept="CSEAIML",
             campus="Gunupur")

collection_name.insert_one(vars(s1))
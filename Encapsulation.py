# class student:
#
#     def __init__(self):
#         self.__name="Aries"
#         self.roll = 52
#
#     def get_name(self):
#         return self.__name
#
#     def get_roll(self):
#         return self.roll
#
#     def set_name(self,name):
#         self.__name = name
#
#
# user1 = student()
# print(user1.get_name())
# user1.set_name("Ashish")
# print(user1.get_name())
# print(user1.get_roll())


import streamlit as st

class Student:
    def _init_(self):
        self.__username = "ashish jena"
        self.__password = "password123"

    def get_name(self):
        return self.__username

    def set_name(self, name):
        self.__username = name

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def check_credentials(self, username, password):
        if username == self._username and password == self._password:
            return "Login successful"
        else:
            return "Login failed"

user1 = Student()

st.title("Login Page")

username_input = st.text_input("Enter username:")
password_input = st.text_input("Enter password:", type="password")

if st.button("Login"):
    result = user1.check_credentials(username_input, password_input)
    st.write(result)


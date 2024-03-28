import streamlit as st
from pymongo import MongoClient
import random


@st.cache_resource
def connection():
    connection_string = "mongodb://localhost:27017/"
    return MongoClient(connection_string)


client = connection()
db = client.banking_db
collection = db.accounts


def generate_account_number():
    return random.randint(10000, 99999)


# Login page
def login_page():
    st.title("Login Page")
    username = st.text_input("Enter your username")
    if st.button("Login"):
        account_number = generate_account_number()
        st.success(f"Account Number: {account_number}")
        if 'username' not in st.session_state:
            st.session_state['username'] = username
        db.users.insert_one({"username": username, "account_number": account_number})


# Main form page
def main_form_page():
    st.title("Main Form Page")
    account_no = st.text_input("Enter account no")
    bank_name = st.text_input("Enter your bank name")
    initial_amount = st.number_input("Enter initial amount")
    deposit_amount = st.number_input("Enter deposit amount")
    credited_amount = st.number_input("Enter credited amount")
    debited_amount = st.number_input("Enter debited amount")

    if st.button("Submit"):
        if 'username' not in st.session_state:
            st.error("Username not found in session state. Please log in first.")
            return

        # Retrieve the user's account number from the database
        user_account_number = db.users.find_one({"username": st.session_state["username"]})["account_number"]

        # Check if the entered account number matches the user's account number
        if account_no == str(user_account_number):
            # Calculate remaining balance
            remaining_balance = initial_amount + deposit_amount - debited_amount + credited_amount

            # Update the form data in your MongoDB collection
            db.users.update_one({"username": st.session_state["username"]}, {"$set": {
                "account_no": account_no,
                "bank_name": bank_name,
                "initial_amount": initial_amount,
                "deposit_amount": deposit_amount,
                "credited_amount": credited_amount,
                "debited_amount": debited_amount,
                "remaining_balance": remaining_balance # Add remaining balance to the update
            }})
            st.success("Form submitted successfully!")
        else:
            st.error("The entered account number does not match your account number. Please check and try again.")



def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Go to", ["Login", "Main Form"])
    if page == "Login":
        login_page()
    elif page == "Main Form":
        main_form_page()


if __name__ == "__main__":
    main()
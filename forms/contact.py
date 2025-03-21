import re
import streamlit as st
import requests

WEBHOOK_URL = "https://connect.pabbly.com/workflow/sendwebhookdata/IjU3NjYwNTY5MDYzMzA0MzU1MjZlNTUzNDUxMzAi_pc"

def is_valid_email(email):
  # Basic regex pattern for email validation
  email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
  return re.match(email_pattern, email) is not None

def contact_form():
  with st.form("contact_form"):
    name = st.text_input("First Name")
    email = st.text_input("Email Adress")
    message = st.text_input("Your Message")
    submit_button = st.form_submit_button("Submit")

    if submit_button:
         if not WEBHOOK_URL :
            st.error(
               "Email service is not setup. Please try again later", icon = "Χ"
            )
            st.stop()

         if not name:
           st.error("Please provide your name.")
           st.stop()
        
         if not email:
           st.error("Please provide your email.")
           st.stop()

         if not is_valid_email(email):
           st.error("Please provide valid email.")
           st.stop()
        
         if not message:
           st.error("Please provide a message.")
           st.stop()

        # Prepare the data payload and send it to the specified webhook URL
        
         data = {"email": email, "name" : name, "message" : message }
         response = requests.post(WEBHOOK_URL, json=data)
    
         if response.status_code == 200:
          st.success("Your message has been sent successfully")
         else:
          st.error("There was an error sending your message")
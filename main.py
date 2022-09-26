import streamlit as st
from hellosign_sdk import HSClient

# Ship logbook record website
st.image('./img/Oceanopedia.png', width=150)
st.title("Ship Logbook Record")
st.write("This is a website to record ship logbook records.")

# Create date and time picker
date = st.date_input("Date")
time = st.time_input("Time")

# Create text input for ship name
ship_name = st.text_input("Ship Name")

# Create streamlit columns
col1, col2 = st.columns(2)

with col1:
    ship_master = st.text_input("Ship's Master")
    ship_safety_officer = st.text_input("Ship's Safety Officer")
    ship_crew_engineer = st.text_input("Ship's Crew Engineer")

with col2:
    ship_master_email = st.text_input("Ship's Master Email")
    ship_safety_officer_email = st.text_input("Ship's Safety Officer Email")
    ship_crew_engineer_email = st.text_input("Ship's Crew Engineer Email")

# On selected date and time, create a logbook record
# if st.button("Create Logbook Record"):
#     st.write("Logbook record created on", date, time)
#     st.write("Ship Name:", ship_name)
#     st.write("Ship's Master:", ship_master)
#     st.write("Ship's Safety Officer:", ship_safety_officer)
#     st.write("Ship's Crew Engineer:", ship_crew_engineer)
#
#     # Create a logbook record
#     logbook_record = f"""
#     Time: {time}
#     Date: {date}
#     Ship_Name: {ship_name}
#     Ship_Master: {ship_master}
#     Ship_Safety_Officer: {ship_safety_officer}
#     Ship_Crew_Engineer: {ship_crew_engineer}
#     """
#
#     # Create a logbook record file
#     with open("logbook_record.txt", "w") as f:
#         f.write(logbook_record)

# Create an instance of HSClient with your API key
client = HSClient(api_key=st.secrets["hs_api_key"])

if st.button("Start Logbook Entry"):
    if ship_master != "" and ship_master_email != "" and ship_safety_officer != "" and ship_safety_officer_email != "" and ship_crew_engineer != "" and ship_crew_engineer_email != "":
        signature_request_id = client.send_signature_request_with_template(
            test_mode=True,
            template_id='9b28e75212e1cc6c2da95ce1a8f9d5ce07fe06fe',
            title='Ship Opertaions Logbook Record',
            subject='Daily ship maintenance and journey record for insurance, safety and crew purposes.',
            message='Required signatories are requested to verify all details carefully and sign the document.',
            signers=[
                { 'role_name': 'Crew Member', 'email_address': ship_crew_engineer_email, 'name': ship_crew_engineer },
                { 'role_name': 'Safety Officer', 'email_address': ship_safety_officer_email, 'name': ship_safety_officer },
                { 'role_name': 'Master', 'email_address': ship_master_email, 'name': ship_master }
            ]
        )
        st.write(signature_request_id)



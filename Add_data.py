import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

def app():
    st.subheader(":point_right: Sales Summary")
    with st.expander("Summary Table"):
        
        conn = st.connection("gsheets", type=GSheetsConnection)

        df = conn.read(worksheet="Sheet1", usecols=list(range(19)),ttl=5)
        df=df.dropna(how="all")

    #Display the DataFrame using st.dataframe with horizontal scrolling
        st.dataframe(df, height=400, width=1200)

    # Form
    st.subheader(":point_right: Add new Entry")
    option_form = st.form("Option Form",clear_on_submit=True)

    # Create three columns inside the form
    col1, col2, col3 = option_form.columns(3)

    # First Column
    with col1:
        Prospect_ID = st.text_input("Prospect ID")
        Industry = st.text_input("Industry")
        Location = st.text_input("Location")
        Organization = st.text_input("Organization")
        Notes = st.text_input("Notes")
        Owner = st.selectbox("Owner", {"", "Gino", "Sachin", "Felci", "Jestna", "Arjun"})

    # Second Column
    with col2:
        Source_of_Lead = st.selectbox("Source of Lead", {"", "Self", "Employee", "Partner", "Event", "Client Initiated"})
        Contacted = st.selectbox("Contacted", {"", "Yes", "No"})
        Prospect_Name = st.text_input("Prospect Name")
        Prospect_Title = st.text_input("Prospect Title")
        Prospect_Phone = st.text_input("Prospect Phone")
        Prospect_Email = st.text_input("Prospect Email")
        Decision_Rights = st.selectbox("Decision Right", {"", "Decision Maker", "Influencer", "Passive", "Junior", "Not Applicable"})

    # Third Column
    with col3:
        Responded = st.selectbox("Responded", {"", "Yes", "No"})
        Interest_Level = st.selectbox("Interest Level", {'', 'High', 'Medium', 'Low'})
        Status = st.selectbox("Status", {'', 'New Lead​', 'Active Discussions​', 'Closed (Won)​', 'Qualified​', 'Proposal​', 'On Hold​', 'Not Responding​', 'Not Applicable​', 'Closed (Lost)​'})
        Follow_Up = st.selectbox("Follow Up", {"", "Yes", "No"})
        Follow_Up_Date = st.text_input("Follow up date")
        Pain_Points = st.text_input("Pain Point")
        Comments= st.text_input("Comments")
        add_data = option_form.form_submit_button(label="Add new Record",)


    # Process the form submission if the button is clicked
    if add_data and len(Prospect_Phone) >= 10 and Prospect_Phone.isdigit():
        # Process the form data here
        st.success("New record added successfully!")

    # When Button is clicked
    if add_data:
  
    # Remove special characters from 'Status'
        clean_status = ''.join(char for char in Status if ord(char) < 128)
        
        data_entry = pd.DataFrame([{
                "Prospect_ID": Prospect_ID,
                "Industry": Industry,
                "Location": Location,
                "Organization": Organization,
                "Notes": Notes,
                "Owner": Owner,
                "Source_of_Lead": Source_of_Lead,
                "Contacted": Contacted,
                "Prospect_Name": Prospect_Name,
                "Prospect_Title": Prospect_Title,
                "Prospect_Phone": Prospect_Phone,
                "Prospect_Email": Prospect_Email,
                "Decision_Rights": Decision_Rights,
                "Responded": Responded,
                "Interest_Level": Interest_Level,
                "Status": clean_status,
                "Follow_Up": Follow_Up,
                "Follow_Up_Date": Follow_Up_Date,
                "Pain_Points": Pain_Points,
                "Comments": Comments}])
        updated_df=pd.concat([df, data_entry], ignore_index=True)
        conn.update(worksheet="Sheet1" , data=updated_df)
    else:
        st.error("Prospect ID is required")

    if len(Prospect_Phone) < 10 or not Prospect_Phone.isdigit():
        st.warning("Please add a valid phone number with at least 10 digits.")
    if '@' not in Prospect_Email:
        st.warning("Please enter a valid email ID.")
    if Industry == "":
        st.warning("Please enter Industry")
    if Location == "":
        st.warning("Please enter Location")
    if Organization == "":
        st.warning("Please enter Organization")
    if Owner == "":
        st.warning("Please enter Owner ")
    if Source_of_Lead == "":
        st.warning("Please enter Source of Lead ")
    if Contacted == "":
        st.warning("Please enter Contacted ")
    if Prospect_Name == "":
        st.warning("Please enter Prospect Name")
    if Decision_Rights == "":
        st.warning("Please enter Decision Right")
    if Responded == "":
        st.warning("Please enter Responded")
    if Interest_Level == "":
        st.warning("Please enter Interest Level")
    if Responded == "":
        st.warning("Please enter Responded")
    if Status == "":
        st.warning("Please enter Status")
    if Follow_Up == "":
        st.warning("Please enter Follow Up")

    st.experimental_rerun()


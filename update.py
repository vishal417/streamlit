import streamlit as st
import pandas as pd
import numpy as np
from streamlit_gsheets import GSheetsConnection

def app():
    st.markdown("Select a Prospect and update their details.")
    conn = st.connection("gsheets", type=GSheetsConnection)

    df = conn.read(worksheet="Sheet1", usecols=list(range(20)),ttl=5)
    df=df.dropna(how="all")

    interest_levels = df["Interest_Level"].dropna().unique().tolist()
    interest_levels.append("")
    interest_levels.sort()
    Status_prodspect = ["","New Lead​", "Active Discussions​", "Closed (Won)​", "Qualified​", "Proposal​", "On Hold​", "Not Responding​", "Not Applicable​", "Closed (Lost)​"]

    prospect_ids = df["Prospect_ID"].tolist()
    Prospect_to_update = st.selectbox("Select a Prospect to Update", options=prospect_ids)
    Prospect_data = df[df["Prospect_ID"] == Prospect_to_update].iloc[0]

    update_form = st.form("update Form")
    Prospect_ID = st.text_input(label="Prospect_ID", value=Prospect_data["Prospect_ID"])
    Industry = st.text_input(label="Industry",value=Prospect_data["Industry"])
    Location = st.text_input(label="Location",value=Prospect_data["Location"])
    Organization = st.text_input(label="Organization",value=Prospect_data["Organization"])
    Notes = st.text_input(label="Notes",value=Prospect_data["Notes"])
    Owner = st.text_input(label="Owner",value=Prospect_data["Owner"])
    Source_of_Lead = st.text_input(label="Source_of_Lead",value=Prospect_data["Source_of_Lead"])
    Contacted = st.text_input(label="Contacted",value=Prospect_data["Contacted"])
    Prospect_Name = st.text_input(label="Prospect_Name",value=Prospect_data["Prospect_Name"])
    Prospect_Title = st.text_input(label="Prospect_Title",value=Prospect_data["Prospect_Title"])
    Prospect_Phone = st.text_input(label="Prospect_Phone",value=Prospect_data["Prospect_Phone"])
    Prospect_Email = st.text_input(label="Prospect_Email",value=Prospect_data["Prospect_Email"])
    Decision_Rights =st.text_input(label="Decision_Rights",value=Prospect_data["Decision_Rights"])
    Responded =st.text_input(label="Responded",value=Prospect_data["Responded"])
    Interest_Level = st.selectbox("Interest Level", options=interest_levels)
    Status = st.selectbox("Status", options=Status_prodspect)
    Follow_Up = st.text_input(label="Follow_Up",value=Prospect_data["Follow_Up"])
    Follow_Up_Date = st.text_input(label="Follow_Up_Date",value=Prospect_data["Follow_Up_Date"])
    Pain_Points = st.text_input(label="Pain_Points",value=Prospect_data["Pain_Points"])
    Comments= st.text_input(label="Comments",value=Prospect_data["Comments"])
    #update button
    update_button = update_form.form_submit_button(label="Update Prospects Details")

    if update_button:
            if not Prospect_ID or not Industry:
                st.warning("Ensure all mandatory fields are filled.")
            else:
                # Removing old entry
                df.drop(
                    df[
                        df["Prospect_ID"] == Prospect_to_update
                    ].index,
                    inplace=True,
                )
                # Creating updated data entry
                updated_prospect_data = pd.DataFrame([{
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
                            "Status": Status,
                            "Follow_Up": Follow_Up,
                            "Follow_Up_Date": Follow_Up_Date,
                            "Pain_Points": Pain_Points,
                            "Comments": Comments}])

                # Adding updated data to the dataframe
                updated_df = pd.concat(
                    [df, updated_prospect_data], ignore_index=True
                )
                conn.update(worksheet="Sheet1", data=updated_df)
                st.success("Prospect details successfully updated!")
                                     
    
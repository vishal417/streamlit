import streamlit as st
import requests
import pandas as pd
from requests_ntlm import HttpNtlmAuth
 
# SharePoint file URL
sharepoint_csv_url = "https://theneostatscom-my.sharepoint.com/:x:/g/personal/vishal_mangalam_theneostats_com/EThXQSqs1O9Jit8AQZDYLu4BjdJue0CPpAoAjO3_waW5ZA?e=8Sfagi&nav=MTVfezAwMDAwMDAwLTAwMDEtMDAwMC0wMDAwLTAwMDAwMDAwMDAwMH0"
 
# Streamlit app
def main():
    st.title("SharePoint CSV Viewer")
 
    # Fetch CSV file
    try:
        # Replace 'your_username' and 'your_password' with actual SharePoint credentials
        username = 'Vishal.Mangalam'
        password = 'Ravi@1234'
 
        # Make a request to SharePoint using NTLM authentication
        response = requests.get(sharepoint_csv_url, auth=HttpNtlmAuth(f"{username}@theneostats.com", password))
 
        if response.status_code == 200:
            csv_content = response.text
 
            # Read CSV content using pandas
            df = pd.read_csv(pd.compat.StringIO(csv_content))
 
            # Display CSV data
            st.write("CSV Data:")
            st.write(df)
        else:
            st.error(f"Failed to fetch CSV file. Status code: {response.status_code}")
 
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching CSV file: {e}")
 
if __name__ == "__main__":
    main()
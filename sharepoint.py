import streamlit as st

# First section: e-mail and password as input
placeholder = st.empty()
with placeholder.container():
  col1, col2, col3 = st.columns(3)
  with col2:
    st.markdown("## **SharePoint connection with Streamlit**")
    st.markdown("--------------")
    username = st.text_input("Your e-mail")
    password = st.text_input("Your password", type="password")
    url = 'https://theneostatscom-my.sharepoint.com/:x:/g/personal/vishal_mangalam_theneostats_com/EThXQSqs1O9Jit8AQZDYLu4BjdJue0CPpAoAjO3_waW5ZA?e=ZJA50i'
    # Save the button status
    Button = st.button("Connect")
    if st.session_state.get('button') != True:
      st.session_state['button'] = Button

from office365.sharepoint.files.file import File
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.authentication_context import AuthenticationContext

# Authentication and connection to SharePoint
def authentication(username, password, url) :
  auth = AuthenticationContext(url) 
  auth.acquire_token_for_user(username, password)
  ctx = ClientContext(url, auth)
  web = ctx.web
  ctx.load(web)
  ctx.execute_query()
  return ctx

# Second section: display results
# Check if the button "Connect" has been clicked
if st.session_state['button'] :                              
  placeholder.empty()
  if "ctx" not in st.session_state :
      st.session_state["ctx"] = authentication(username,   
                                               password, 
                                               url)
  
  st.write("Authentication: successfull!")
  st.write("Connected to SharePoint: **{}**".format( st.session_state["ctx"].web.properties['Title']))
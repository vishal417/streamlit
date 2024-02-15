import streamlit as st
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

from streamlit_option_menu import option_menu
import dashboardd, Add_data, update, delete

# Define user credentials and their roles
user_credentials = {
    "admin": {"password": "admin", "role": "admin"},
    "user1": {"password": "password1", "role": "user"},
    # Add more users as needed
}

st.set_page_config(page_title="Neostats sales Prospect", page_icon=":chart_with_upwards_trend:", layout="wide")

def creds_entered():
    username = st.session_state["user"].strip()
    password = st.session_state["passwd"].strip()
    
    if username in user_credentials and password == user_credentials[username]["password"]:
        st.session_state["authenticated"] = True
        st.session_state["user_role"] = user_credentials[username]["role"]
    else:
        st.session_state["authenticated"] = False
        st.error("Invalid username or password")

def authenticate_user():
    if "authenticated" not in st.session_state:
        st.text_input(label="Username :", value="", key="user", on_change=creds_entered)
        st.text_input(label="Password :", value="", key="passwd", type="password", on_change=creds_entered)
        return False
    else:
        if st.session_state["authenticated"]:
            return True
        else:
            st.text_input(label="Username :", value="", key="user", on_change=creds_entered)
            st.text_input(label="Password :", value="", key="passwd", type="password", on_change=creds_entered)
            return False

def run():
    user_role = st.session_state.get("user_role", "user")  # Default to "user" role if not set

    if user_role == "admin":
        admin_functions()
    elif user_role == "user":
        user1_functions()

def admin_functions():
    st.sidebar.image("neostats.jpg", caption="NeoStats Analytics Solutions PVT LTD")
    with st.sidebar:
        app = option_menu(
            menu_title='Menu',
            options=['Dashboard', 'Add Record', 'Update', 'Delete'],
            icons=['person-circle'],
            menu_icon='N',
            default_index=0,
            styles={
                "container": {"padding": "2!important", "background-color": 'black'},
                "icon": {"color": "white", "font-size": "15px"},
                "nav-link": {"color": "white", "font-size": "15px", "text-align": "left", "margin": "0px",
                             "--hover-color": "blue"},
                "nav-link-selected": {"background-color": "#02ab21"},
            }
        )

    if app == "Add Record":
            Add_data.app()
    elif app == "Dashboard":
            dashboardd.app()
    elif app == "Update":
            update.app()
    elif app == "Delete":
            delete.app()

def user1_functions():
    st.header("User1 Functions")
    # Add your user1-specific functionality here

if authenticate_user():

    run()

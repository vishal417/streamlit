import streamlit as st
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

def app():
    import streamlit as st
    from streamlit_gsheets import GSheetsConnection
    
    conn = st.connection("gsheets", type=GSheetsConnection)

    df = conn.read(worksheet="Sheet1", usecols=list(range(19)),ttl=5)
    df=df.dropna(how="all")
    

    

    # Sidebar layout
    st.subheader("Filter Data")

    col1, col2, col3, col4 = st.columns((4))

    with col1:
        # Create for Industry
        Industry = st.multiselect("Industry", df["Industry"].unique())
        if not Industry:
            df2 = df.copy()
        else:
            df2 = df[df["Industry"].isin(Industry)]

    with col2:
        # Create for Organization
        Organization = st.multiselect("Organization", df2["Organization"].unique())
        if not Organization:
            df3 = df2.copy()
        else:
            df3 = df2[df2["Organization"].isin(Organization)]

    with col3:
        # Create for Location
        Location = st.multiselect("Location", df3["Location"].unique())
        if not Location:
            df4 = df3.copy()
        else:
            df4 = df3[df3["Location"].isin(Location)]

    with col4:
        # Create for Owner
        Owner = st.multiselect("Owner", df4["Owner"].unique())
        if not Owner:
            df5 = df4.copy()
        else:
            df5 = df4[df4["Owner"].isin(Owner)]
    if not Industry and not Organization and not Location and not Owner:
        filtered_df = df
    elif not Organization and not Location and not Owner:
        filtered_df = df[df["Industry"].isin(Industry)]
    elif not Industry and not Location and not Owner:
        filtered_df = df2[df2["Organization"].isin(Organization)]
    elif not Industry and not Organization and not Owner:
        filtered_df = df3[df3["Location"].isin(Location)]
    elif not Industry and not Organization and not Location:
        filtered_df = df4[df4["Owner "].isin(Owner)]
    elif Industry and Organization and Location:
        filtered_df = df5[
            df["Industry"].isin(Industry)
            & df2["Organization"].isin(Organization)
            & df3["Location"].isin(Location)
        ]
    elif Industry and Location and Owner:
        filtered_df = df5[
            df["Industry"].isin(Industry)
            & df3["Location"].isin(Location)
            & df4["Owner "].isin(Owner)
        ]
    elif Industry and Organization and Owner:
        filtered_df = df5[
            df["Industry"].isin(Industry)
            & df2["Organization"].isin(Organization)
            & df4["Owner "].isin(Owner)
        ]
    elif Organization and Location and Owner:
        filtered_df = df5[
            df2["Organization"].isin(Organization)
            & df3["Location"].isin(Location)
            & df4["Owner "].isin(Owner)
        ]
    elif Industry and Organization:
        filtered_df = df5[
            df["Industry"].isin(Industry) & df2["Organization"].isin(Organization)
        ]
    elif Industry and Location:
        filtered_df = df5[df["Industry"].isin(Industry) & df3["Location"].isin(Location)]
    elif Industry and Owner:
        filtered_df = df5[df["Industry"].isin(Industry) & df4["Owner"].isin(Owner)]
    elif Organization and Location:
        filtered_df = df5[
            df2["Organization"].isin(Organization) & df3["Location"].isin(Location)
        ]
    elif Organization and Owner:
        filtered_df = df5[
            df2["Organization"].isin(Organization) & df4["Owner "].isin(Owner)
        ]
    elif Location and Owner:
        filtered_df = df5[df3["Location"].isin(Location) & df4["Owner "].isin(Owner)]
    else:
        filtered_df = df5[
            df["Industry"].isin(Industry)
            & df3["Location"].isin(Location)
            & df4["Owner "].isin(Owner)
        ]

    col1, col2, col3, col4 = st.columns((4))

    with col1:
        total_organizations = filtered_df['Organization'].nunique()
        st.markdown(f"<p style='font-size: small; font-weight: bold;'>Total Number of Organizations:</p>",
                    unsafe_allow_html=True)
        st.info(f"{total_organizations}")

    with col2:
        total_Prospect_Name = filtered_df['Prospect_Name'].nunique()
        st.markdown(f"<p style='font-size: small; font-weight: bold;'>Total Number of Prospects:</p>",
                    unsafe_allow_html=True)
        st.info(f"{total_Prospect_Name}")

    with col3:
        # Count the occurrences and create a table
        Interest_Level = st.multiselect("Interest Level", df5["Interest_Level"].unique())
        if not Interest_Level:
            df6 = df5.copy()
        else:
            df6 = df5[df5["Interest_Level"].isin(Interest_Level)]
    filtered_df = df6

    
    with col4:
        st.markdown(f"<p style='font-size: small; font-weight: bold;'>Interest Count:</p>", unsafe_allow_html=True)
        # Count the occurrences and create a table
        Interest_level_counts = pd.crosstab(index=filtered_df['Interest_Level'], columns='count')
        Interest_level_transposed_counts = Interest_level_counts.transpose()
        interest_order = ['High', 'Medium', 'Low']
        Interest_level_transposed_counts_sorted = Interest_level_transposed_counts.reindex(columns=interest_order,
                                                                                          fill_value=0)
        st.markdown(Interest_level_transposed_counts_sorted.to_markdown(index=False), unsafe_allow_html=True)
    


    col1, col2 = st.columns((5, 1))

    with col1:
        st.markdown(f"<p style='font-size: small; font-weight: bold;'>Status Count:</p>", unsafe_allow_html=True)

        # Count the occurrences and create a table
        Status_counts = pd.crosstab(index=filtered_df['Status'], columns='count')
        Status_transposed_counts = Status_counts.transpose()

        # Specify the desired order of Status categories
        Status_order = ['New Lead', 'Active Discussions', 'Closed (Won)', 'Qualified', 'Proposal', 'On Hold',
                        'Not Responding', 'Not Applicable', 'Closed (Lost)']
        Status_transposed_counts_sorted = Status_transposed_counts.reindex(columns=Status_order, fill_value=0)

        # Display the Status Count table
        st.markdown(Status_transposed_counts_sorted.to_markdown(index=False), unsafe_allow_html=True)

        # Sidebar filter for Status
        Status = st.multiselect("Status", df6["Status"].unique())

        # Apply the filter to the DataFrame
        if not Status:
            df7 = df6.copy()
        else:
            df7 = df6[df6["Status"].isin(Status)]

    import streamlit as st

    # Assuming filtered_df is already defined

    st.subheader(":point_right: Sales Summary")
    with st.expander("Summary Table"):
        df_sample = df7

        # Display the DataFrame using st.dataframe with horizontal scrolling
        st.dataframe(df_sample, height=400, width=1200)

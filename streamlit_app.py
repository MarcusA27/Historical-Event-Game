import pandas as pd
import streamlit as st
import time

st.set_page_config(
    page_title="Event Guesser",   # Title that shows in the browser tab
    page_icon="🎮",        # Can be emoji or path to an image file
    layout="centered",     # Optional: "centered" or "wide"
)

if "streak" not in st.session_state:
    st.session_state.streak = 0

df = pd.read_csv('World Important Dates.csv')
pd.set_option("display.max_columns", None)
df = df.drop(["Outcome", "Important Person/Group Responsible", "Affected Population", "Place Name"], axis=1)
df_filtered = df[df["Date"].str.isnumeric()]
df_filtered['Name of Incident'] = df_filtered['Name of Incident'].str.replace('Unknown', '-')



for events in df_filtered:

    random_row1 = df_filtered.sample(n=1)
    date_1 = int(random_row1["Year"].iloc[0])
    random_row2 = df_filtered.sample(n=1)
    date_2 = int(random_row2["Year"].iloc[0])

    if abs(date_2 - date_1) <= 21:
        break

with st.container():

    st.image('https://mtv-main-assets.mountvernon.org/files/styles/original/s3/callouts/surrendering-his-commission-web-4.jpg.webp?VersionId=349ROqBSKJY.oG982oe1BcVzWZKs6nzc&itok=Agt9F4CR')
    st.subheader("Which Historical Event Came First?")
    st.divider()

with st.container():
    st.write(f"Streak: {st.session_state.streak}")
    def check_one():
        if date_1 > date_2:
            col1.write("Correct")
            col1.write(date_1)
            col1.write(date_2)
            st.session_state.streak +=1

        else:
            col1.write("Incorrect")
            col1.write(date_1)
            col1.write(date_2)
            st.session_state.streak = 0

    def check_two():
        if date_2 > date_1:
            col1.write("Correct")
            col1.write(date_1)
            col1.write(date_2)
            st.session_state.streak += 1

        else:
            col1.write("Incorrect")
            col1.write(date_1)
            col1.write(date_2)
            st.session_state.streak = 0


    col1, col2 = st.columns([1, 1])
    col1.button(f"{random_row1["Name of Incident"].iloc[0]}",on_click=check_one, width=700)
    col2.button(f"{random_row2["Name of Incident"].iloc[0]}\n", on_click=check_two, width=700)





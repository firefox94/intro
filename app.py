import streamlit as st

## pages config ##
about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True
)

ml_page = st.Page(
    page="views/ml_models.py",
    title="Classification traning models",
    icon=":material/adb:"
)

chatbot_page = st.Page(
    page="views/chatbot.py",
    title="Chat Bot",
    icon="🤖"
)

# Navigation
pg = st.navigation({
    "Info": [about_page],
    "Projects": [ml_page, chatbot_page]
})

# Author
# st.logo("Link logo")
st.sidebar.text("Made by firefox94 😻")

# Run Navigation
pg.run()
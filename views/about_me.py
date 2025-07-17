import streamlit as st

@st.dialog("Contact Me")
def show_contact():
    st.write("📧 haviet20@gmail.com")
    st.write("🔗 https://www.linkedin.com/in/hanguyen94/")

st.markdown("""
    <style>
    .title {
        text-align: center;
        color: #4CAF50;
        font-size: 48px;
    }
    </style>
    <h1 class="title">About Me 🕵️‍♀️</h1>
    """, unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("assets/avatar2.jpg", width=220)
with col2:
    st.title("Nguyen Ba Viet Ha", anchor=False)
    st.write(
        "Senior Data Scientist / Senior Data Analyst"
    )
    
    if st.button("📫 Contact Me"):
        show_contact()
        
# Experience
st.write("\n")
st.subheader("Working Experience", anchor=False)
st.write("""
    - 5+ years in Data Domain with LPBank, VPBank and MBAgeas
    - Strong hand-on building ML models and AI applications
    - Good problems solving and detecing bussiness pain points
    """)

# Skills
st.write("\n")
st.subheader("Skill Sets", anchor=False)
st.write("""
    - Programming: Python, SQL
    - Data visualization: PowerBI
    - Modeling: Suppervise (Regression & Classification), Unsuppervise (Clustering & PCA)
    - Database: MSSQL, Postgres, Oracle
    """)

# Projects
st.write("\n")
st.subheader("Projects", anchor=False)
st.write("""
    - Fraud Detection
    - Up sales/Cross sales
    - Churn prediction
    - ChatBot
    """)
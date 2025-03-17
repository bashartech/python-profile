import streamlit as st

# pages

about_page = st.Page(
    page="views/about.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)
project_1_page = st.Page(
    page="views/dashboard.py",
    title="Sales Dashboard",
    icon=":material/bar_chart:",
)
project_2_page = st.Page(
    page="views/chatbot.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)

#navigate

pg = st.navigation(
    {
        "Info":[about_page],
        "Projects":[project_1_page, project_2_page],
    }
)

# SHARED ON ALL PAGES

st.logo("assets/pzpro.PNG")
st.sidebar.markdown("Made by Bashar")

# Run
pg.run()


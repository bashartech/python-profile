import streamlit as st

from forms.contact import contact_form

@st.dialog("Contact Me")
def show_contact_form():
   contact_form()

# Hero

col1, col2 = st.columns(2, gap= "small", vertical_alignment="center")
with col1:
    st.image("./assets/web services.png", width=230)
with col2: 
    st.title("M.Bashar Sheikh", anchor=False)
    st.write("Professional Web Developer with experties in Nextjs and Typescript"
             )
if st.button("Contact Me"):
    show_contact_form()

# EXPERIENCE AND QUALIFICATION

st.write("\n")
st.subheader("Experience and Qualification", anchor = False)
st.write(
    """
I am a passionate and skilled creative professional with a robust background in front end web development specializing in crafting exceptional user experiences through coding and design. My expertise lies in HTML CSS JavaScript and TypeScript alongside advanced frameworks like Next.js Tailwind CSS ShadCN UI and Radix UI.
"""
)

# SKILLS
st.write("\n")
st.subheader("Hard Skills", anchor = False)
st.write(
    """
I am a dedicated creative professional specializing in front end web development and UI/UX design, with expertise in HTML, CSS, JavaScript, TypeScript, Next.js, Tailwind CSS, ShadCN UI, and Radix UI
"""
)
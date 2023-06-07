from pathlib import Path

import streamlit as st
from PIL import Image


#--Path Settings--
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "templates" / "main.css"
resume_file = current_dir / "assets" / "Resume.pdf"
profile_pic = current_dir / "assets" / "Profile-Pic.jpg"


#--General Settings--
PAGE_TITLE = "Digital Resume | Jason Kim"
PAGE_ICON = ":wave:"
NAME = "Jason Kim"
DESCRIPTION = """
Csin3 student, solo game developer/designer. Aspiring to be a great game developer and to gather/work with a team. 
I am also interested in other fields of computer science such as engineering and software. 
"""
EMAIL = "jason.t.kim@icloud.com"
SOCIAL_MEDIA = {
    "LinkedIn": "linkedin.com/in/jason-kim-6ab8b2279",
    "GitHub": "https://github.com/DawnSovereign",
    "Twitter": "https://twitter.com/DawnyGamer",
}
PROJECTS = {
    "Python Group Project - Look at the air quality, weather, wind, and earthquakes: "
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


#--Load CSS, PDF & Profil pic--
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

#--Hero Section--
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📬", EMAIL)

    #--Social Links--
    st.write("#")
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")

#--Experience & Qualifications
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
    - Completed the first year of the Csin3 program learning about computer programming and data analytics.
    - Learned Python web development and GUI programming.
    - Learned C++ Object Oriented Programming.
    - Completed first year of Csin3 program. 
    - Great at working in groups and project managing and learning new things fast when needed. 
    """
)


#--Skills--
st.write("#")
st.subheader("Hard Skills")
st.write(
    """
    - Programming: Python (GUI programming, web development, and image manipulation.) C++ (Object Oriented Programming and SFML) C# (MonoGame)
    - American Red Cross trained first aid/cpr/aed.
    """
)

#--Work History--
st.write("#")
st.subheader("Work History")
st.write("---")

#--job 1
st.write("**Lifeguard | Monterey Sports Center**")
st.write("June 2019 - April 2023")
st.write(
    """
    Trained to perform recues when needed and trained in American Red Cross first aid/cpr/aed training and certified. 
    Set up the pool room to be ready in the mornings and cleared up and put equipment away during closing.
    During the shifts I had to keep watch of all patrons and made sure everyone followed the rules and stayed safe. 
    """
)

#--job 2
st.write("#")
st.write("**Volunteer Worker | Monterey FairGrounds**")
st.write("December 2018 - December 2019")
st.write(
    """
    On the 23nd of December 2018 and 2019, volunteered to help with the Christmas dinner set up for the homeless at the Monterey FairGrounds. 
    Helped to set up clothing and helped prepare the tables and decor for the area where the homeless can enjoy their food that would be served to them.
    """
)

#--Projects & Accomplishments
st.write("#")
st.subheader("Projects & Accomplishments")
st.write("---")
for project in PROJECTS:
    st.write(project)

st.write("---")
st.write("#")
st.write("Website made by Jason Kim")
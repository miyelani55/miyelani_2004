import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import io
import os

# Set page title
st.set_page_config(page_title="Aluwani Budeli - Portfolio", layout="wide")

# Define profile picture path
PROFILE_PIC_PATH = "profile_pic.jpg"

# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Profile", "Publications", "Vlog", "Contact"],
)

# Function to load profile picture
def load_profile_picture():
    if os.path.exists(PROFILE_PIC_PATH):
        return Image.open(PROFILE_PIC_PATH)
    return None

# Function to save profile picture
def save_profile_picture(uploaded_file):
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        image.save(PROFILE_PIC_PATH)
        return image
    return None

# Sections based on menu selection
if menu == "Profile":
    st.title("Profile")
    
    # Profile picture upload in sidebar
    st.sidebar.header("Profile Picture")
    
    # Load existing profile picture
    existing_pic = load_profile_picture()
    
    uploaded_pic = st.sidebar.file_uploader("Upload a profile picture", type=["jpg", "jpeg", "png"])
    
    # Save new picture if uploaded
    if uploaded_pic is not None:
        current_pic = save_profile_picture(uploaded_pic)
        st.sidebar.success("Profile picture updated successfully!")
    else:
        current_pic = existing_pic
    
    # Create two columns for layout: one for image, one for summary
    col1, col2 = st.columns([1, 2])
    
    # Profile details
    name = "Aluwani Tshimangadzo Budeli"
    courses = [
        {"name": "Bachelor's Degree Biochemistry & Microbiology", "year": "2020 - 2024"},
        {"name": "Postgraduate Certificate In Education (PGCE)", "year": "2024 - 2025"}
    ]
    institution = "University of Venda"
    
    # Professional summary
    professional_summary = """Highly motivated professional with a strong foundation in Biochemistry and Microbiology (BSc, 2024) 
    and a qualification in Education (PGCE, 2025). Currently pursuing Honours in Science Education. 
    Seeking a role that leverages my scientific expertise in biochemistry or microbiology, or a position 
    in education where I can inspire learners. 6 months of experience working with learners has sparked 
    my passion for making science accessible. Let's connect and explore opportunities."""
    
    # Top skills
    top_skills = """• Laboratory techniques and safety protocols
    • Molecular biology techniques (PCR, DNA extraction, gel electrophoresis)
    • Biochemical assays (ELISA, chromatography, spectroscopy)
    • Enzyme kinetics and protein analysis"""
    
    with col1:
        if current_pic is not None:
            # Display saved image
            st.image(current_pic, width=250, caption="Profile Picture")
        else:
            # Placeholder image if none uploaded
            st.image("https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png", 
                     width=250, caption="Upload your picture (sidebar)")
        
        # Add option to remove picture
        if current_pic is not None:
            if st.button("Remove Profile Picture"):
                if os.path.exists(PROFILE_PIC_PATH):
                    os.remove(PROFILE_PIC_PATH)
                st.rerun()
        
        st.write("")
        st.write("")
        st.markdown("### Top Skills")
        st.markdown(top_skills)
    
    with col2:
        st.write(f"**Name:** {name}")
        st.write(f"**Courses Completed:**")
        for course in courses:
            st.write(f"  • {course['name']} ({course['year']})")
        st.write(f"**Institution:** {institution}")
        st.markdown("### Professional Summary")
        st.write(professional_summary)

elif menu == "Publications":
    st.title("Publications")
    st.sidebar.header("Upload and Filter")

    # Upload publications file
    uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")
    if uploaded_file:
        publications = pd.read_csv(uploaded_file)
        st.dataframe(publications)

        # Add filtering for year or keyword
        keyword = st.text_input("Filter by keyword", "")
        if keyword:
            filtered = publications[
                publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
            ]
            st.write(f"Filtered Results for '{keyword}':")
            st.dataframe(filtered)
        else:
            st.write("Showing all publications")

        # Publication trends
        if "Year" in publications.columns:
            st.subheader("Publication Trends")
            year_counts = publications["Year"].value_counts().sort_index()
            st.bar_chart(year_counts)
        else:
            st.write("The CSV does not have a 'Year' column to visualize trends.")
    else:
        st.info("Please upload a CSV file to view publications.")

elif menu == "Contact":
    # Add a contact section
    st.header("Contact Information")
    email = "aluwanibudeli79@gmail.com"

    st.write(f"You can reach me at **{email}**.")
    
    # Optional: Add a contact form
    st.markdown("---")
    st.subheader("Send a Message")
    with st.form("contact_form"):
        name_input = st.text_input("Your Name")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send")
        if submitted:
            st.success(f"Thank you {name_input}, your message has been sent! (Demo)")

elif menu == "Vlog":
    st.title("Vlog / Blog")
    st.info("Vlog section coming soon! Here you can share videos, tutorials, or science outreach content.")
    # Placeholder for future vlog content
    st.write("🎥 Future content: Lab tutorials, science explainers, educational videos, and more!")

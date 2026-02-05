import streamlit as st
import pandas as pd

# -----------------------------
# App Configuration
# -----------------------------
st.set_page_config(
    page_title="Researcher Profile",
    layout="wide"
)

# -----------------------------
# Researcher Info (Static)
# -----------------------------
name = "Luyanda Nqobani Mpanza"
field = "Computer Science"
institution = "University of Zululand"
email = "luyanda.mpanza@unizulu.ac.za"

# Initialise session state
if "research_data" not in st.session_state:
    st.session_state.research_data = {}

# -----------------------------
# TITLE
# -----------------------------
st.title("Researcher Profile Page")

# -----------------------------
# PROFILE OVERVIEW
# -----------------------------
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

st.image(
    "https://media.istockphoto.com/id/1312417734/photo/social-networking-service-streaming-video-communication-network-3d-illustration.jpg",
    caption="Digital research and data-driven systems"
)

# -----------------------------
# RESEARCH INFORMATION INPUT
# -----------------------------
st.header("Research Information")

with st.form("research_form"):
    research_title = st.text_input(
        "Research Title",
        value=st.session_state.research_data.get("title", "")
    )

    research_interests = st.text_area(
        "Research Interests",
        placeholder="e.g. Data visualisation, educational technology, machine learning",
        value=st.session_state.research_data.get("interests", "")
    )

    methodology = st.selectbox(
        "Research Methodology",
        [
            "Quantitative",
            "Qualitative",
            "Mixed Methods",
            "Experimental",
            "Computational / Simulation-based"
        ]
    )

    tools = st.multiselect(
        "Tools & Technologies Used",
        [
            "Python",
            "Streamlit",
            "Pandas",
            "NumPy",
            "Plotly",
            "Machine Learning",
            "SQL",
            "Cloud Platforms"
        ],
        default=st.session_state.research_data.get("tools", [])
    )

    description = st.text_area(
        "Research Description / Abstract",
        height=180,
        value=st.session_state.research_data.get("description", "")
    )

    submitted = st.form_submit_button("Save Research Information")

    if submitted:
        st.session_state.research_data = {
            "title": research_title,
            "interests": research_interests,
            "methodology": methodology,
            "tools": tools,
            "description": description
        }
        st.success("Research information saved successfully.")

# -----------------------------
# DISPLAY RESEARCH SUMMARY
# -----------------------------
if st.session_state.research_data:
    st.header("Research Summary")
    st.write(f"**Title:** {st.session_state.research_data.get('title', '')}")
    st.write(f"**Methodology:** {st.session_state.research_data.get('methodology', '')}")
    st.write(f"**Tools:** {', '.join(st.session_state.research_data.get('tools', []))}")
    st.write("**Description:**")
    st.write(st.session_state.research_data.get("description", ""))

# -----------------------------
# PUBLICATIONS
# -----------------------------
st.header("Publications")

uploaded_file = st.file_uploader(
    "Upload a CSV file of publications",
    type="csv"
)

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    keyword = st.text_input("Filter publications by keyword")

    if keyword:
        filtered = publications[
            publications.apply(
                lambda row: keyword.lower() in row.astype(str).str.lower().values,
                axis=1
            )
        ]
        st.subheader(f"Filtered Results for '{keyword}'")
        st.dataframe(filtered)
else:
    st.info("Upload a CSV file to display publications.")

# -----------------------------
# PUBLICATION TRENDS
# -----------------------------
st.header("Publication Trends")

if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.warning("The CSV file must include a 'Year' column.")
else:
    st.info("Upload a publications CSV file to view trends.")

# -----------------------------
# CONTACT
# -----------------------------
st.header("Contact Information")
st.write(f"**Researcher:** {name}")
st.write(f"**Email:** {email}")
st.write(f"**Institution:** {institution}")

st.markdown(
    "For academic collaboration, supervision discussions, or research-related inquiries, "
    "please use the contact details above."
)

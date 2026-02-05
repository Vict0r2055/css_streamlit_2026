import streamlit as st
import pandas as pd

# -----------------------------
# App Configuration
# -----------------------------
st.set_page_config(
    page_title="Researcher Profile | Luyanda Mpanza",
    layout="wide"
)

# -----------------------------
# Researcher Info (Static)
# -----------------------------
name = "Luyanda Nqobani Mpanza"
field = "Computer Science (Natural Language Processing)"
institution = "University of Zululand"
email = "luyanda.mpanza@unizulu.ac.za"

# -----------------------------
# Session State
# -----------------------------
if "research_data" not in st.session_state:
    st.session_state.research_data = {
        "title": "Morpheme-Aware Tokenization for isiZulu Language Models",
        "interests": (
            "African language NLP, isiZulu morphology, morpheme-aware tokenization, "
            "low-resource language modeling, transformer-based language models, "
            "fair and inclusive AI"
        ),
        "methodology": "Computational / Simulation-based",
        "tools": [
            "Python",
            "Streamlit",
            "Pandas",
            "Machine Learning",
            "Deep Learning / Transformers"
        ],
        "description": (
            "This research investigates the integration of linguistically grounded "
            "morphological knowledge into subword tokenization for isiZulu, a "
            "morphologically rich and low-resource African language. "
            "The study proposes a hybrid rule-based and BPE-constrained tokenizer "
            "derived from the SADiLaR isiZulu Morphological Annotation Protocol. "
            "The tokenizer is evaluated within a full transformer-based language "
            "modeling pipeline, comparing standard BPE against morpheme-aware BPE "
            "using metrics such as fertility, morphological edit distance, boundary "
            "F1 score, perplexity, and BLEU. The work contributes toward more "
            "linguistically faithful and equitable language technologies for "
            "African languages."
        )
    }

# -----------------------------
# TITLE
# -----------------------------
st.title("Researcher Profile")

# -----------------------------
# PROFILE OVERVIEW
# -----------------------------
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field:** {field}")
st.write(f"**Institution:** {institution}")

st.image(
    "https://media.istockphoto.com/id/1312417734/photo/social-networking-service-streaming-video-communication-network-3d-illustration.jpg",
    caption="Language technology, computation, and data-driven research",
    use_column_width=True
)

# -----------------------------
# RESEARCH INFORMATION
# -----------------------------
st.header("Research Information")

with st.form("research_form"):
    research_title = st.text_input(
        "Research Title",
        value=st.session_state.research_data["title"]
    )

    research_interests = st.text_area(
        "Research Interests",
        value=st.session_state.research_data["interests"]
    )

    methodology = st.selectbox(
        "Research Methodology",
        [
            "Quantitative",
            "Qualitative",
            "Mixed Methods",
            "Experimental",
            "Computational / Simulation-based"
        ],
        index=4
    )

    tools = st.multiselect(
        "Tools & Technologies Used",
        [
            "Python",
            "Streamlit",
            "Pandas",
            "NumPy",
            "Machine Learning",
            "Deep Learning / Transformers",
            "SQL",
            "Cloud Platforms"
        ],
        default=st.session_state.research_data["tools"]
    )

    description = st.text_area(
        "Research Description / Abstract",
        height=220,
        value=st.session_state.research_data["description"]
    )

    submitted = st.form_submit_button("Save Research Information")

    if submitted:
        st.session_state.research_data.update({
            "title": research_title,
            "interests": research_interests,
            "methodology": methodology,
            "tools": tools,
            "description": description
        })
        st.success("Research information updated.")

# -----------------------------
# RESEARCH SUMMARY
# -----------------------------
st.header("Research Summary")

st.markdown(f"### {st.session_state.research_data['title']}")
st.write(f"**Methodology:** {st.session_state.research_data['methodology']}")
st.write(f"**Tools:** {', '.join(st.session_state.research_data['tools'])}")
st.markdown("**Abstract**")
st.write(st.session_state.research_data["description"])

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
    st.dataframe(publications, use_container_width=True)

    keyword = st.text_input("Filter publications by keyword")

    if keyword:
        filtered = publications[
            publications.apply(
                lambda row: keyword.lower() in row.astype(str).str.lower().values,
                axis=1
            )
        ]
        st.subheader(f"Filtered Results for '{keyword}'")
        st.dataframe(filtered, use_container_width=True)
else:
    st.info("Upload a CSV file (e.g. Title, Year, Venue, Authors).")

# -----------------------------
# PUBLICATION TRENDS
# -----------------------------
st.header("Publication Trends")

if uploaded_file and "Year" in publications.columns:
    year_counts = publications["Year"].value_counts().sort_index()
    st.bar_chart(year_counts)
elif uploaded_file:
    st.warning("CSV must include a 'Year' column.")

# -----------------------------
# CONTACT
# -----------------------------
st.header("Contact Information")
st.write(f"**Researcher:** {name}")
st.write(f"**Email:** {email}")
st.write(f"**Institution:** {institution}")

st.markdown(
    "For academic collaboration, supervision discussions, "
    "or research on African language technologies and NLP, "
    "please use the contact details above."
)

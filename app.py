import streamlit as st
import pandas as pd

# -----------------------------
# App Configuration
# -----------------------------
st.set_page_config(
    page_title="Research Profile | Luyanda Mpanza",
    layout="wide"
)

# -----------------------------
# TITLE
# -----------------------------
st.title("Research Profile")
st.caption("Morpheme-Aware Tokenization for isiZulu")

# -----------------------------
# SIDEBAR NAVIGATION
# -----------------------------
section = st.sidebar.radio(
    "Navigate",
    [
        "Overview",
        "Research Problem",
        "Methodology",
        "Tokenizer Pipeline",
        "Evaluation Metrics",
        "Contribution & Impact"
    ]
)

# -----------------------------
# OVERVIEW
# -----------------------------
if section == "Overview":
    st.header("Researcher Information")

    st.markdown("""
    **Name:** Luyanda Nqobani Mpanza  
    **Field:** Computer Science (Natural Language Processing)  
    **Institution:** University of Zululand  
    **Email:** luyanda.mpanza@unizulu.ac.za  
    """)

    st.subheader("Research Title")
    st.markdown("**Morpheme-Aware Tokenization for isiZulu Language Models**")

# -----------------------------
# RESEARCH PROBLEM
# -----------------------------
elif section == "Research Problem":
    st.header("Research Problem")

    level = st.radio(
        "Select explanation depth",
        ["High-level", "Technical"]
    )

    if level == "High-level":
        st.markdown("""
        isiZulu is morphologically complex, with rich prefixation and
        agglutination. Standard subword tokenization methods such as BPE
        ignore linguistic structure, often producing fragmentations that
        break valid morpheme boundaries. This negatively affects language
        modelling and text generation.
        """)
    else:
        st.markdown("""
        Standard BPE operates purely on frequency-based merges without
        awareness of isiZulu morphological templates. This leads to
        invalid cross-morpheme merges, inflated token fertility, and
        reduced generalization. The research introduces morphology-aware
        constraints derived from SADiLaR protocols to prevent such merges.
        """)

# -----------------------------
# METHODOLOGY
# -----------------------------
elif section == "Methodology":
    st.header("Methodology")

    steps = st.multiselect(
        "Select components of the methodology",
        [
            "Morphological rule formalisation",
            "Rule-based tokenizer implementation",
            "BPE constraint integration",
            "Transformer language model training",
            "Comparative evaluation"
        ],
        default=[
            "Morphological rule formalisation",
            "Rule-based tokenizer implementation",
            "BPE constraint integration",
            "Transformer language model training",
            "Comparative evaluation"
        ]
    )

    for step in steps:
        st.markdown(f"- {step}")

# -----------------------------
# TOKENIZER PIPELINE
# -----------------------------
elif section == "Tokenizer Pipeline":
    st.header("Tokenizer Pipeline")

    stage = st.selectbox(
        "View pipeline stage",
        [
            "Input Text",
            "Morphological Segmentation",
            "BPE-Constrained Subword Learning",
            "Final Token Output"
        ]
    )

    example = "ngiyabathanda"

    if stage == "Input Text":
        st.code(example)

    elif stage == "Morphological Segmentation":
        st.code("ngi-ya-ba-thand-a")

    elif stage == "BPE-Constrained Subword Learning":
        st.code("ngi | ya | ba | thand | a")

    else:
        st.code(["ngi", "ya", "ba", "thand", "a"])

# -----------------------------
# EVALUATION METRICS
# -----------------------------
elif section == "Evaluation Metrics":
    st.header("Evaluation Metrics")

    metric = st.selectbox(
        "Select metric",
        [
            "Token Fertility",
            "Morphological Edit Distance",
            "Boundary F1 Score",
            "Perplexity",
            "BLEU Score"
        ]
    )

    explanations = {
        "Token Fertility": "Average number of tokens per word. Lower is better.",
        "Morphological Edit Distance": "Measures divergence from gold morpheme boundaries.",
        "Boundary F1 Score": "Precision and recall of predicted morpheme boundaries.",
        "Perplexity": "Model uncertainty in predicting the next token.",
        "BLEU Score": "Quality of generated text compared to reference output."
    }

    st.info(explanations[metric])

# -----------------------------
# CONTRIBUTION & IMPACT
# -----------------------------
elif section == "Contribution & Impact":
    st.header("Contribution & Impact")

    impact = st.checkbox("Show research impact")

    if impact:
        st.markdown("""
        - First linguistically constrained BPE tokenizer for isiZulu.
        - Demonstrates measurable improvements in language modelling.
        - Supports responsible and inclusive AI for African languages.
        - Aligns with national AI strategy and language preservation efforts.
        """)


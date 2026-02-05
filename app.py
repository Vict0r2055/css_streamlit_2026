import streamlit as st

# -----------------------------
# App Configuration
# -----------------------------
st.set_page_config(
    page_title="Research Profile | Luyanda Mpanza",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("Research Profile")

# -----------------------------
# Researcher Information
# -----------------------------
st.header("Researcher Information")

st.markdown("""
**Name:** Luyanda Nqobani Mpanza  
**Field:** Computer Science (Natural Language Processing)  
**Institution:** University of Zululand  
**Email:** luyanda.mpanza@unizulu.ac.za  
""")

# -----------------------------
# Research Title
# -----------------------------
st.header("Research Title")

st.markdown("""
**Morpheme-Aware Tokenization for isiZulu Language Models**
""")

# -----------------------------
# Research Focus
# -----------------------------
st.header("Research Focus")

st.markdown("""
This research addresses the limitations of standard subword tokenization
methods when applied to isiZulu, a morphologically rich and low-resource
African language.

Conventional Byte Pair Encoding (BPE) methods ignore linguistic structure,
often splitting words in ways that violate valid morpheme boundaries.
This work proposes a linguistically grounded, morpheme-aware tokenization
approach that integrates explicit isiZulu morphological rules into the
tokenization process.
""")

# -----------------------------
# Methodology
# -----------------------------
st.header("Methodology")

st.markdown("""
The study follows a **computational and experimental methodology**:

- Formalisation of isiZulu morphological segmentation rules based on the
  SADiLaR isiZulu Morphological Annotation Protocol.
- Development of a deterministic, rule-based morphological tokenizer.
- Integration of morphology-aware constraints into a BPE-based subword
  learning framework.
- Training of transformer-based language models using both standard BPE
  and morpheme-aware BPE tokenizers.
- Comparative evaluation using intrinsic and extrinsic metrics.
""")

# -----------------------------
# Evaluation
# -----------------------------
st.header("Evaluation Strategy")

st.markdown("""
The proposed tokenizer is evaluated within a full language modelling
pipeline using the following metrics:

- Token fertility to measure segmentation efficiency.
- Morphological edit distance to assess alignment with gold morpheme
  boundaries.
- Boundary precision, recall, and F1 score.
- Cross-entropy loss and perplexity for language modelling performance.
- BLEU score to evaluate generated text quality.
""")

# -----------------------------
# Tools and Technologies
# -----------------------------
st.header("Tools and Technologies")

st.markdown("""
- Python  
- Rule-based morphological parsing  
- Byte Pair Encoding (BPE)  
- Transformer-based language models  
- PyTorch / deep learning frameworks  
""")

# -----------------------------
# Contribution
# -----------------------------
st.header("Research Contribution")

st.markdown("""
This research contributes:

- A linguistically grounded morpheme-aware tokenizer for isiZulu.
- A reproducible integration strategy for linguistic rules and subword
  tokenization.
- Empirical evidence that morphology-aware tokenization improves language
  modelling for agglutinative African languages.
- A step toward fairer and more inclusive language technologies for
  low-resource languages.
""")

# -----------------------------
# Contact
# -----------------------------
st.header("Contact")

st.markdown("""
For academic collaboration or research inquiries:

**Email:** luyanda.mpanza@unizulu.ac.za  
**Institution:** University of Zululand
""")

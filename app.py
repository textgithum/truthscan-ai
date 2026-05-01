import streamlit as st
import joblib
from PIL import Image
import re
import pandas as pd
import requests

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="TruthScan - AI Lie Detection",
    page_icon="🧠",
    layout="wide"
)

# =====================================
# GLOBAL STYLING
# =====================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #020617, #0f172a, #1e293b);
    color: white;
}

/* HEADER */
.header-container {
    display: flex;
    align-items: center;
    padding: 20px;
    border-radius: 15px;
    background: linear-gradient(135deg, #020617, #0f172a, #1e293b);
    margin-bottom: 25px;
}

.logo {
    font-size: 40px;
    margin-right: 15px;
}

.title {
    font-size: 34px;
    font-weight: bold;
}

.title span {
    color: #3b82f6;
}

.subtitle {
    font-size: 14px;
    color: #94a3b8;
    margin-top: -5px;
}

/* SIDEBAR CARD */
.sidebar-card {
    background: linear-gradient(135deg, #020617, #0f172a, #1e40af);
    padding: 20px;
    border-radius: 12px;
    color: white;
    margin-bottom: 20px;
}

.sidebar-title {
    font-size: 22px;
    font-weight: bold;
}

.sidebar-title span {
    color: #3b82f6;
}

.sidebar-subtitle {
    font-size: 16px;
    color: #94a3b8;
    margin-bottom: 10px;
}

.sidebar-text {
    font-size: 14px;
    color: #cbd5f5;
}

/* BUTTON */
.stButton>button {
    background: linear-gradient(90deg, #3b82f6, #06b6d4);
    color: white;
    border-radius: 8px;
    height: 45px;
    width: 100%;
    border: none;
}

/* TEXT AREA */
.stTextArea textarea {
    background-color: #1e293b;
    color: white;
    border-radius: 10px;
}

/* METRIC BOX */
[data-testid="stMetric"] {
    background-color: #1e293b;
    padding: 15px;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# HEADER
# =====================================

st.markdown("""
<div class="header-container">
    <div class="logo">🧠</div>
    <div>
        <div class="title">Truth<span>Scan</span></div>
        <div class="subtitle">AI LIE DETECTION SYSTEM</div>
    </div>
</div>
""", unsafe_allow_html=True)

# =====================================
# SIDEBAR
# =====================================

with st.sidebar:

    st.markdown("""
    <div class="sidebar-card">
        <div class="sidebar-title">Advanced <span>Lie Detection</span></div>
        <div class="sidebar-subtitle">Powered by AI & NLP</div>
        <div class="sidebar-text">
        Our advanced AI model analyzes text patterns, language behavior, 
        and context to detect the probability of deception.
        </div>
    </div>
    """)

    if st.button("🔄 Reset App"):
        st.session_state.clear()
        st.rerun()

# =====================================
# LOAD MODEL
# =====================================

model = joblib.load("lie_detection_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# =====================================
# FUNCTIONS
# =====================================

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def predict_text(text):
    cleaned = clean_text(text)
    vec = vectorizer.transform([cleaned])

    pred = model.predict(vec)[0]
    prob = model.predict_proba(vec)[0]

    truth = prob[0] * 100
    lie = prob[1] * 100

    # ✅ FIXED
    if pred == 'T':
        final = "Truth"
    else:
        final = "Lie"

    confidence = max(truth, lie)

    return final, truth, lie, confidence

# =====================================
# OCR FUNCTION (API ONLY)
# =====================================

API_KEY = "3c30888a6988957"

def extract_text(file):
    try:
        response = requests.post(
            "https://api.ocr.space/parse/image",
            files={"file": file.getvalue()},
            data={
                "apikey": API_KEY,
                "language": "eng",
                "isOverlayRequired": False
            }
        )

        result = response.json()

        if result.get("ParsedResults"):
            text = result["ParsedResults"][0].get("ParsedText", "")
        else:
            return "⚠️ No text detected"

        # CLEAN TEXT
        text = text.replace("\n", " ")
        text = re.sub(r'[^a-zA-Z\s]', ' ', text)
        text = re.sub(r'\s+', ' ', text).strip()

        return text

    except:
        return "⚠️ OCR failed"

# =====================================
# TABS
# =====================================

tab1, tab2 = st.tabs(["✍️ Text Analysis", "🖼 Image Analysis"])

# =====================================
# TEXT TAB
# =====================================

with tab1:

    st.subheader("Enter Text")

    user_input = st.text_area("Type your message here...")

    if st.button("🔍 Analyze Text"):

        if user_input.strip():

            with st.spinner("Analyzing..."):
                pred, truth, lie, conf = predict_text(user_input)

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Prediction", pred)
                st.metric("Confidence", f"{conf:.2f}%")

            with col2:
                st.metric("Truth %", f"{truth:.2f}%")
                st.metric("Lie %", f"{lie:.2f}%")

            st.subheader("📊 Probability Distribution")

            df = pd.DataFrame({
                "Type": ["Truth", "Lie"],
                "Probability": [truth, lie]
            })

            st.bar_chart(df.set_index("Type"))

# =====================================
# IMAGE TAB
# =====================================

with tab2:

    st.subheader("Upload Image")

    uploaded = st.file_uploader("Upload Image", type=["png","jpg","jpeg"])

    if uploaded:

        img = Image.open(uploaded)

        st.image(img, caption="Uploaded Image", use_container_width=True)

        with st.spinner("Extracting text..."):
            text = extract_text(uploaded)

        st.subheader("📄 Extracted Text")
        st.write(text)

        if st.button("🔍 Analyze Image"):

            with st.spinner("Analyzing..."):
                pred, truth, lie, conf = predict_text(text)

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Prediction", pred)
                st.metric("Confidence", f"{conf:.2f}%")

            with col2:
                st.metric("Truth %", f"{truth:.2f}%")
                st.metric("Lie %", f"{lie:.2f}%")

            st.subheader("📊 Probability Distribution")

            df = pd.DataFrame({
                "Type": ["Truth", "Lie"],
                "Probability": [truth, lie]
            })

            st.bar_chart(df.set_index("Type"))
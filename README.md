# 🧠 TruthScan – AI Powered Lie Detection System

TruthScan is an AI-powered lie detection and text analysis system built using Machine Learning, NLP, OCR, and Streamlit.
The application analyzes textual statements and predicts whether the statement is likely to be **Truth** or **Lie** based on linguistic patterns.

It also supports screenshot-based chat analysis using OCR (Optical Character Recognition).

---

# 🌐 Live Project

### 🔗 Project URL

https://truthscan-ai-ekk7g9kaotxrakk4dnz7mi.streamlit.app/

---

# 🚀 Features

## ✅ Single Text Analysis

Analyze a single statement and predict:

* Truth Probability
* Lie Probability
* Confidence Score

---

## ✅ Screenshot OCR Analysis

Upload chat screenshots/images and:

* Extract text using Tesseract OCR
* Clean noisy OCR text
* Analyze extracted messages
* Predict truth/lie probability

---

## ✅ Interactive Modern UI

* Futuristic neon dark theme
* Responsive Streamlit dashboard
* AI-style prediction cards
* Upload section for screenshots

---

## ✅ Machine Learning + NLP

The project uses:

* TF-IDF Vectorization
* Logistic Regression / Random Forest
* Text preprocessing
* NLP-based deception indicators

---

# 🛠️ Technologies Used

* Python
* Streamlit
* Scikit-learn
* Pandas
* NumPy
* Tesseract OCR
* OpenCV
* Pillow
* Joblib

---

# 📂 Project Structure

```bash id="7w5tpa"
TruthScan/
│
├── app.py
├── lie_detection_model.pkl
├── tfidf_vectorizer.pkl
├── requirements.txt
├── README.md
└── screenshots/
```

---

# ▶️ Run Application

```bash id="y2l4ew"
streamlit run app.py
```

---

# 📊 Model Information

* Dataset Size: 500+ labeled statements
* Labels:

  * T → Truth
  * F → Lie
* Accuracy Achieved:

  * Logistic Regression → ~80%
  * Random Forest → ~79%

---

# 🖼️ OCR Workflow

1. Upload Screenshot
2. Extract Text using OCR
3. Clean OCR Noise
4. Normalize Text
5. Predict Truth/Lie

---

# 📸 Screenshots

## Dashboard UI

<img width="1910" height="864" alt="image" src="https://github.com/user-attachments/assets/bebebfb1-fe6b-404f-a22d-99956551e5e4" />


## OCR Analysis

<img width="1919" height="869" alt="image" src="https://github.com/user-attachments/assets/1a73a3a0-434e-4f94-b139-cbdad26b9729" />


---

# 🔮 Future Improvements

* Real-time voice lie detection
* Deep learning models
* Emotion analysis
* Multi-language support
* Advanced chatbot integration
* User authentication system

---

# 👩‍💻 Developed By

**Nikki Ram**
BE – Artificial Intelligence & Machine Learning
Alard College of Engineering & Management, Pune

---

# 📜 License

This project is for educational and research purposes only.

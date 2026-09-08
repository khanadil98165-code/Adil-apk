import streamlit as st
import google.generativeai as genai
from PIL import Image

# App Title
st.title("Adil - AI Stock & Trading Analyzer")
st.write("Apne trading chart ki photo upload karein aur instant analysis payein.")

# Gemini API Key Setup
API_KEY = "YOUR_GEMINI_API_KEY"  # Yahan apni free API Key daalein
genai.configure(api_key=API_KEY)

# Image Uploader
uploaded_file = st.file_uploader("Chart Image Choose Karein...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Chart', use_column_width=True)
    
    if st.button('Analyze Chart'):
        with st.spinner('Chart analyze ho raha hai...'):
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            prompt = """
            Aap ek expert stock aur trading analyst hain. Is image ko dhyan se dekhein aur bataein:
            1. Is Stock/Crypto/Forex ka naam kya hai (agar visible hai)?
            2. Konsa Chart Pattern ya Indicator ban raha hai?
            3. Trend kya hai (Bullish/Bearish/Neutral)?
            4. Potential Entry Point, Stop Loss, aur Target Levels kya ho sakte hain?
            5. Key Risk and Recommendation.
            Jawab simple Hinglish mein dein.
            """
            
            response = model.generate_content([prompt, image])
            st.subheader("Analysis Results:")
            st.write(response.text)
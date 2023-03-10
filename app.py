import streamlit as st
from PIL import Image
import requests
import pandas as pd
import os
import json
#
image_path = "image.png"
image = Image.open(image_path)

st.set_page_config(page_title="Language Detection App", layout="centered")
st.image(image, caption='Language Detection App')
#
# page header
st.title(f"Language Detection App")
with st.form("Generate"):
   text1 = st.text_input("Input Text supported : [English,German,French,Swedish,Russian,Arabic,Spanish,Portuguese,Italian,Dutch,Turkish,Greek,Hindi,Dutch]. Enter text here")
   submit = st.form_submit_button("Detect Language")
   #
   if submit:    
        print(text1)
        #
        with open("input.txt", "wb") as f:
            f.write(text1.encode("utf-8"))
        os.chmod("input.txt", 0o777)
        # Keyword Extraction API
        
        url = "https://app.aimarketplace.co/api/marketplace/models/detect-language-from-the-text-df617b80/predict/"
        payload={'data': open('input.txt','rb')}
        headers = {'Authorization': 'Api-Key fJmK0Mnu.6CdR5aMw1wxTBMJ7gp0qhwMcS5NlMjuw'}

        response = requests.request("POST", url, headers=headers, files=payload)
        #
        print(response.text)
        # output header
        st.header("Language Detected")
        # output results
        st.success(response.text.split("detected ")[1].split("}")[0].split(":")[1].replace('"',"",).replace('\\',""))
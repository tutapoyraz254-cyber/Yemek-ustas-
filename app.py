import streamlit as st
import replicate
import os

st.set_page_config(page_title="Poyraz AI", page_icon="🎬")
st.title("👨‍🍳 Poyraz AI Yemek Ustası")
replicate_key = st.secrets["REPLICATE_API_TOKEN"]
os.environ["REPLICATE_API_TOKEN"] = replicate_key
prompt = st.text_input("Videonun içinde ne olsun?", "A cute dragon eating a burger")
if st.button("🚀 Videoyu Pişir"):
    with st.spinner("Poyraz hazırlıyor..."):
        try:
            output = replicate.run(
                "lucataco/animate-diff:be10bc105ee697818300263675f3a0a6d09c6ba37b12d99d3d3a0e676bd80f5d",
                input={"prompt": prompt + ", high quality"}
            )
            st.video(output)
        except Exception as e:
            st.error(f"Hata: {e}")
          

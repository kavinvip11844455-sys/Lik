import streamlit as st
import openai
from fpdf import FPDF
import datetime

st.set_page_config(page_title="Love Insurance Kompany", page_icon="💘")

st.title("💘 Love Insurance Kompany 💘")
st.caption("Powered by kavin.r | Manasu odanjadhu ku claim kedayadhu 😂")

client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

name1 = st.text_input("Peru 1:", "Chairman")
name2 = st.text_input("Peru 2:", "CEO Kavin")
chat = st.text_area("Recent Chat:", "dei 600/600 score sollu")

if st.button("🔮 Breakup Risk Score Paaru"):
    prompt = f"Act as Chairman Alazhu Moon Araki. Analyze chat between {name1} and {name2}: '{chat}'. Give breakup risk score 0-100. Be funny, Tamil + English. End with G.O. number."
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    result = response.choices[0].message.content
    st.write(result)
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Love Insurance Kompany Certificate", ln=1, align='C')
    pdf.cell(200, 10, txt=f"{name1} + {name2}", ln=1, align='C')
    pdf.multi_cell(0, 10, txt=result)
    pdf.output("certificate.pdf")
    
    with open("certificate.pdf", "rb") as f:
        st.download_button("📜 Insurance Certificate Download Pannu", f, "certificate.pdf")

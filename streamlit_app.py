import streamlit as st
import openai
from fpdf import FPDF
import base64

st.set_page_config(page_title="Love Insurance AI", page_icon="💔", layout="centered")
st.title("💘 Chairman Alazhu Moon Love Insurance AI 💘")
st.caption("Powered by kavin.r | G.O. No. 600/600.49: Manasu odanjadhu ku claim kedayadhu 😂")

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.header("1. Unga Love Details ah Sollu")
col1, col2 = st.columns(2)
with col1:
    name1 = st.text_input("Unnoda Peru", "600/600")
with col2:
    name2 = st.text_input("Lover Peru", "Thangamey")

chat_history = st.text_area("Last 5 Chat Copy Paste Pannu",
                            "A: Hi da\nB: Hmm\nA: Saptiya?\nB: Busy\nA: Oh ok\nB: Seen",
                            height=150)

if st.button("🔮 Breakup Risk Score Paaru", type="primary"):
    if not chat_history:
        st.error("Chat history podu da, summa score varadhu")
    else:
        with st.spinner("Chairman AI yosikudhu..."):
            try:
                prompt = f"""
                Nee oru comedy Relationship Insurance AI. Indha couple oda chat ah paathu
                0-100 kulla Breakup Risk Score kudu.
                0 = Kalyanam confirm, 100 = Innaiku night eh unfriend.
                Reason 1 line la Tamil la funny ah sollu. Chairman Alazhu Moon style la sollu.

                Couple: {name1} & {name2}
                Chat: {chat_history}

                Format: Score: XX | Reason:...
                """

                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=80
                )
                result = response.choices[0].message.content
                score = int(result.split('|')[0].split(':')[1].strip())

                st.subheader("2. AI Report Vandhuruchu 📜")
                if score < 30:
                    st.success(f"**Risk Score: {score}/100** 🟢 Low Risk")
                    st.balloons()
                    premium = "₹0/month - Free da, neenga 600/600 couple"
                elif score < 70:
                    st.warning(f"**Risk Score: {score}/100** 🟡 Medium Risk")
                    premium = "₹99/month - Sanda podama irunga"
                else:
                    st.error(f"**Risk Score: {score}/100** 🔴 High Risk")
                    premium = "₹999/month - Emergency Counselling venum"

                st.info(f"**Chairman Reason:** {result.split('|')[1].strip()}")
                st.write(f"**Suggested Love Insurance Premium:** {premium}")

                st.subheader("3. Love Insurance Certificate Eduthuko 📜")
                if st.button("Download Certificate PDF"):
                    pdf = FPDF()
                    pdf.add_page()
                    pdf.set_font("Arial", 'B', 16)
                    pdf.cell(0, 10, "Chairman Alazhu Moon Love Insurance Co.", 0, 1, 'C')
                    pdf.set_font("Arial", '', 12)
                    pdf.cell(0, 10, f"Certified That {name1} & {name2}", 0, 1, 'C')
                    pdf.cell(0, 10, f"Breakup Risk Score: {score}/100", 0, 1, 'C')
                    pdf.cell(0, 10, f"Premium: {premium}", 0, 1, 'C')
                    pdf.cell(0, 10, "Disclaimer: Idhu velayattu ku mattum. Claim pannina adichiduven 😂", 0, 1, 'C')
                    pdf_output = pdf.output(dest='S').encode('latin-1')
                    b64 = base64.b64encode(pdf_output).decode()
                    href = f'<a href="data:application/octet-stream;base64,{b64}" download="Love_Insurance_{name1}_{name2}.pdf">📥 Certificate Download Pannu</a>'
                    st.markdown(href, unsafe_allow_html=True)

            except Exception as e:
                st.error(f"AI ku kovam vandhuruchu: {e}. API Key Secrets la pottiya nu paaru")

st.divider()
st.caption("⚠️ Disclaimer: Idhu entertainment purpose ku mattum. IRDAI approved illa 😂")

import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Love Insurance Kompany 600/600", page_icon="💘", layout="centered")

# Gemini setup
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("💘 Love Insurance Kompany 600/600")
st.subheader("Chairman Alazhu Moon Araki ⚖️🐠🪙")
st.caption("Powered by kavin.r | Manasu odanjadhu ku claim kedayadhu 😂")

st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    name1 = st.text_input("Peru 1:", placeholder="Chairman")
with col2:
    name2 = st.text_input("Peru 2:", placeholder="CEO Kavin")

situation = st.text_area("Recent Chat:", placeholder="dei 600/600 score sollu")

if st.button("🔮 Breakup Risk Score Paaru", type="primary"):
    if not name1 or not name2 or not situation:
        st.error("DEI 600/600! Ella column ah fill pannu da!")
    else:
        with st.spinner("Chairman Alazhu Moon Araki Case ah aaraayuraar... ⚖️"):
            prompt = f"""
            Nee Chairman Alazhu Moon Araki. Love Insurance Kompany oda Chairman. 
            Unoda style: Comedy ah pesuva, "600/600" nu solluva, "DEI" nu thituva, gavel ah kuthuva.
            G.O. nu order poduva.

            Case:
            Peru 1: {name1}
            Peru 2: {name2}
            Situation: {situation}

            4 vishayam sollu:
            1. **Breakup Risk Score:** 0/600 to 600/600. 600 = full breakup.
            2. **Chairman Order G.O. No. XXX/600:** 2 line advice kudu.
            3. **Kompany Verdict:** "Policy Approve" or "Claim Reject" or "Premium Kattunga"
            4. **Chairman Punch:** "DEI" nu start panni oru comedy dialogue.

            Tamil la sollu. Emojis podu. 600/600 style la irukkanum.
            """
            
            try:
                response = model.generate_content(prompt)
                st.success("Chairman Order Vandhuduchu! 600/600 ⚖️")
                st.markdown(response.text)
                st.balloons()
                st.info("**Disclaimer:** Idhu comedy app da 600/600 😂")
            except Exception as e:
                st.error(f"DEI 600/600! Chairman busy: {str(e)}")
                st.warning("Secrets la GEMINI_API_KEY sariya iruka nu paaru.")

st.sidebar.markdown("### 📜 Kompany Rules")
st.sidebar.markdown("1. Kaadhal = Investment")
st.sidebar.markdown("2. Sanda = Market Crash") 
st.sidebar.markdown("3. Chairman Sonna 600/600")
st.sidebar.markdown("---")
st.sidebar.markdown("**Powered by Gemini AI** 🔮")
st.sidebar.markdown("**Free Plan** ✅ 0/600 Cost")

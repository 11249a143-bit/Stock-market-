import streamlit as st

def render_header():
    st.markdown("""
    <style>
    .block-container{max-width:1500px;padding-top:1.7rem}
    .hero{padding:1.5rem 1.8rem;border-radius:18px;
    background:linear-gradient(115deg,#10233f,#174a70);
    border:1px solid #285b7b;margin-bottom:1.2rem}
    .hero h1{color:#fff;margin:0;font-size:2.2rem}
    .hero p{color:#d6eafa;margin:.45rem 0 0}
    </style>
    <div class="hero"><h1>📈 Stock Market Analyzer</h1>
    <p>Historical prices, technical indicators, performance and risk analytics.</p></div>
    """, unsafe_allow_html=True)

import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Kalkulator Usia Kehamilan",
    page_icon="logo.png",
    layout="centered"    
)

st.markdown(
    """

    <style>
        .main {{
            background-color: #f8fcfd;
        }}
        h1, h2, h3, h4 {{
            color: #2a9cc1;
        }}
        stButton>button {{
            background-color: #2a9cc1;
            color: white;
            border-radius: 8px;
        }}
        .footer {{
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            padding: 10px;
            background-color: #e6f4f8;
            text-align: center;
            color: #2a9cc1;
            font-size: 14px
        }}
    </style>
    <div class="footer>
        2025 IT RSIA Respati - Build with Love
    </div>
    """,
    unsafe_allow_html=True
)

st.image("logo.png", width=120)
st.markdown("<h3 style='text-align: center; color: #2a9cc1;'>Build With Love IT RSIA Respati</h3>", unsafe_allow_html=True)
st.markdown("---")


st.title ("Kalakulator usia kehamilan")
st.write ("Masukan **Hari Pertama haid Terakhir (HPHT)** untuk menghitung usia kehamilan dan HPL")

hpht = st.date_input("Tanggal HPHT")

if hpht :
    hari_ini = datetime.today().date()
    usia_hari = (hari_ini - hpht).days
    minggu = usia_hari // 7
    sisa_hari = usia_hari % 7

    hpl = hpht + timedelta(days=280)

    st.subheader("Hasil Perhitungan")
    st.write(f"- Usia kehamilan: **{minggu} Minggu {sisa_hari} Hari**")
    st.write(f"- Perkiraan tanggal perasalinan (HPL): **{hpl.strftime('%d %B %Y')}**")
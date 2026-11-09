
import streamlit as st

st.set_page_config(
    page_title="Geotextile Calculator",
    page_icon="🏗️"
)

st.title("🏗️ Geotextile Cost Calculator")
st.write("Aplikasi perhitungan biaya material")

# Input dari pengguna
luas = st.number_input(
    "Luas Geotextile (m²)",
    min_value=0.0,
    value=600.0
)

harga = st.number_input(
    "Harga per m² (Rp)",
    min_value=0,
    value=25000
)

ongkir = st.number_input(
    "Biaya Pengiriman (Rp)",
    min_value=0,
    value=200000
)

# Tombol perhitungan
if st.button("Hitung Total Biaya"):

    if luas <= 0:
        st.error("Luas harus lebih dari 0!")
    else:
        subtotal = luas * harga

        if luas >= 500:
            diskon = 0.10
        elif luas >= 200:
            diskon = 0.05
        else:
            diskon = 0

        nilai_diskon = subtotal * diskon
        total = subtotal - nilai_diskon + ongkir

        st.subheader("Hasil Perhitungan")
        st.write(f"Subtotal: Rp {subtotal:,.0f}")
        st.write(f"Diskon: {diskon:.0%}")
        st.write(f"Nilai Diskon: Rp {nilai_diskon:,.0f}")
        st.write(f"Ongkir: Rp {ongkir:,.0f}")

        st.success(f"Total Biaya: Rp {total:,.0f}")

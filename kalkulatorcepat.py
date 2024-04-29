import streamlit as st
from streamlit_option_menu import option_menu 

def main():
    st.sidebar.header("Navigasi")
    selected = st.sidebar.selectbox("Pilih halaman:", ["Kalkulator Cepat Menghitung Kadar Cu", "Anggota Tim"])

    if selected == "Anggota Tim":
        show_team_members()
    elif selected == "Kalkulator Cepat Menghitung Kadar Cu":
        calculate_cu_content()

def show_team_members():
    st.title('Anggota Kelompok 6')
    st.markdown('<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
                unsafe_allow_html=True)
    st.write('''
1. Andiani Putri Wijiyanti (2320507)
2. Azizah lintang Maylya (2320511)
3. Dimas Farrel Arunajati (2320519)
4. Fadhlurahman Rayyandani Shafwan (2320522)
5. Putri Chalis Lestari (2320544)
6. Ratu Amalia Zahara (2320551)''')

def calculate_cu_content():
    st.title('Kalkulator Cepat Menghitung Kadar Cu')  

    st.markdown('---')
    st.markdown('''Kalkulator cepat ini dibuat bertujuan untuk memudahkan teman-teman menghitung 
            kadar Cu dalam sampel makanan yang sudah dianalisis melalui Spektrofotometri Serapan Atom (SAA).''')

    st.markdown(
        '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
        unsafe_allow_html=True
    )

    y = st.number_input("Masukkan nilai y:", step=0.0001)
    st.write('Hasil dari absorbansi adalah=', y)
    a = st.number_input("Masukkan nilai a:", step=0.0001)
    st.write('Hasil dari intersept adalah=', a)
    b = st.number_input("Masukkan nilai b:", step=0.0001)
    st.write('Hasil dari slope adalah=', b)

    y2 = st.number_input("Masukkan nilai y2:", step=0.0001)
    st.write('Hasil dari absorbansi adalah=', y2)
    a2 = st.number_input("Masukkan nilai a2:", step=0.0001)
    st.write('Hasil dari intersept adalah=', a2)
    b2 = st.number_input("Masukkan nilai b2:", step=0.0001)
    st.write('Hasil dari slope adalah=', b2)

    hitung_x = st.button("Hitung kadar c terukur")

    if hitung_x:
        x = (y - a) / b
        x2 = (y2 - a2) / b2
        rata_rata_x = (x + x2) / 2
        st.write(f"Hasil perhitungan x = {rata_rata_x} (mg/L)")

    st.markdown(
        '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
        unsafe_allow_html=True
    )

    c_terukur = st.number_input("Masukkan kadar C terukur (mg/L)", step=0.0001)
    st.write('Hasil dari konsentrasi terukur adalah=', c_terukur)
    v = st.number_input("Masukkan nilai V (L):", step=0.0001)
    st.write('Hasil dari volume adalah=', v)
    FP = st.number_input("Masukkan nilai FP:", step=0.0001)
    st.write('Hasil dari FP adalah=', FP)
    bobot_sampel = st.number_input("Masukkan nilai bobot sampel (gram):", step=0.0001)
    st.write('Hasil dari bobot sampel adalah=', bobot_sampel)

    hitung_cu = st.button("Hitung kadar cemaran Cu")

    if hitung_cu:
        kadar_cemaran_cu = (c_terukur * v * FP) / (bobot_sampel * 0.001)
        st.write(f"Hasil perhitungan kadar cemaran Cu = {kadar_cemaran_cu} ppm")

if __name__ == '__main__':
    main()
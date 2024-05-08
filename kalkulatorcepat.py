import streamlit as st
import pandas as pd


def main():
    st.sidebar.header("Navigasi")
    selected = st.sidebar.selectbox("Pilih halaman:", ["Anggota Tim", "Informasi Tambahan", "Pendahuluan", "Petunjuk Penggunaan Aplikasi","Kalkulator Cepat Menghitung Kadar Cu (untuk sampel padatan)", "Kalkulator Cepat Menghitung Kadar Cu (untuk sampel cairan)"])

    if selected == "Anggota Tim":
        show_team_members()
    elif selected == "Informasi Tambahan":
        show_informasitambahan()
    elif selected == "Pendahuluan":
        show_pendahuluan()
    elif selected == "Kalkulator Cepat Menghitung Kadar Cu (untuk sampel padatan)":
        calculate_cu_content()
    elif selected == "Petunjuk Penggunaan Aplikasi":  
        show_penggunaan_aplikasi()  
    elif selected == "Kalkulator Cepat Menghitung Kadar Cu (untuk sampel cairan)":
        calculate_cu_liquid()

def show_informasitambahan():
    # Tabel informasi tambahan
    st.title("Informasi Tambahan")
    default_kalkulatorcepat = {
        "Permen": "2.0 mg/kg",
        "Susu formula": "20.0 mg/kg",
        "Susu UHT": "0.02 mg/kg",
        "Tepung Terigu": "10 mg/kg",
        "Produk Siap Konsumsi": "20 mg/kg", 
        "Makanan Hasil Laut": "1.0 mg/kg", 
        "Sayuran Segar": "2.0 mg/kg",
        "Kopi": "30 mg/kg",
        "Air mineral": "0.02 mg/L",
        "Pasta coklat": "15.0 mg/kg",
        "Keju": "0.02 mg/kg",
        "Yogurt": "0.20 mg/kg",
        "Minuman berperisa berkarbonisasi": "0.05 mg/kg",
        "Eskrim": "20.0 mg/kg",
        "Baso ikan beku": "0.3 mg/kg",
        "Kripik kulit ikan": "0.3 mg/kg"
    }

    df = pd.DataFrame({
        "Sampel Produk": list(default_kalkulatorcepat.keys()),
        "Maksimal Kadar Cu": list(default_kalkulatorcepat.values())
    })

    # Garis pembatas berwarna-warni
    st.markdown(
        '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
        unsafe_allow_html=True
    )

    st.write("Berikut beberapa daftar maksimal kadar Cu pada produk pangan menurut SNI:")
    st.dataframe(df)

def show_pendahuluan():
    st.title("Pendahuluan")
    st.markdown('<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
                unsafe_allow_html=True)
    st.write("Logam Cu merupakan logam berat essensial yang dibutuhkan oleh tubuh dalam jumlah yang kecil, namun bila jumlah yang masuk ke dalam tubuh berlebihan akan berubah fungsi menjadi zat racun bagi tubuh. Keracunan Cu dapat menyebabkan gangguan pada jalur pernapasan. Pada makanan dan minuman sering terdapat unsur-unsur yang tidak mempunyai nilai nutrisi. Adanya unsur-unsur tersebut selalu dihubungkan dengan sifat-sifat yang tidak diinginkan dan kadang-kadang beracun sehingga membahayakan kesehatan konsumen. Oleh karena itu, diperlukan syarat-syarat untuk industri makanan dan minuman agar produksinya tidak membahayakan bagi konsumen, sehingga tujuan pembuatan web ini untuk menghitung kadar cemaran logam Cu yang telah dilakukan pengujian cemaran logam sesuai dengan SNI.")

def show_penggunaan_aplikasi():
    st.title("Petunjuk Penggunaan Aplikasi")
    st.markdown('<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
                unsafe_allow_html=True)
    st.write('''
1. Pilih halaman yang diperlukan
2. Untuk memlilih kalkulator cepat dapat dipilih sesuai yang user inginkan
3. Masukkan volume atau bobot sampel yang akan di konversi (opsional)
4. Masukkan nilai absorbansi, slope, dan intersept
5. lalu klik kolom hitung kadar Cterukur
6. Masukkan cterukur, volume labu takar, faktor pengenceran, dan bobot sampel atau volume sampel
7. Klik kolom hitung kadar cemaran Cu''')            

def show_team_members():
    st.title('۫  ..˖💬໒꒰ྀ Anggota Kelompok 6꒱ྀིঌ₊')
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
    st.title('۫𓈒 ׄ ੭୧ Kalkulator Cepat Menghitung Kadar Cu pada sampel yang berwujud padatan ྀঌ .. ')  

    st.markdown('<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
                unsafe_allow_html=True)
    st.markdown('''Kalkulator cepat ini dibuat bertujuan untuk memudahkan teman-teman menghitung 
            kadar Cu (tembaga) dalam sampel pangan yang sudah dianalisis melalui Spektrofotometer Serapan Atom (SSA).''')

    st.header('Konversi Satuan (Opsional)')
    st.write("Konversi ini digunakan untuk mengubah dari miligram ke gram dan dari mililiter ke liter")
    st.markdown('<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
                unsafe_allow_html=True)
    angka = st.number_input("Masukkan angka yang ingin di konversi:", step=0.0001)
    st.write('angka yang diinput adalah=', angka)

    hitung_angka = st.button("Hitung konversi angka")

    if hitung_angka:
        angka = angka/1000
        st.write(f"Hasil perhitungan angka = {angka}")

    st.header('Perhitungan Kadar Cterukur')
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

    st.header("Cemaran Kadar Cu Dalam Sampel")

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

def calculate_cu_liquid():
    st.title('۫𓈒 ׄ ੭୧ Kalkulator Cepat Menghitung Kadar Cu pada sampel yang berwujud cairan ྀঌ .. ')  
    st.markdown('<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
                unsafe_allow_html=True)
    st.markdown('''Kalkulator cepat ini dibuat bertujuan untuk memudahkan teman-teman menghitung 
            kadar Cu (tembaga) dalam sampel pangan yang sudah dianalisis melalui Spektrofotometer Serapan Atom (SSA).''')

    st.header('Konversi Satuan (Opsional)')
    st.write("Konversi ini digunakan untuk mengubah dari miligram ke gram dan dari mililiter ke liter")
    st.markdown('<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
                unsafe_allow_html=True)
    angka = st.number_input("Masukkan angka yang ingin di konversi:", step=0.0001)
    st.write('angka yang diinput adalah=', angka)

    hitung_angka = st.button("Hitung konversi angka")

    if hitung_angka:
        angka = angka/1000
        st.write(f"Hasil perhitungan angka = {angka}")

    st.header('Perhitungan Kadar Cterukur')
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

    st.header("Cemaran Kadar Cu Dalam Sampel")

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
    volume_sampel = st.number_input("Masukkan nilai volume sampel (L):", step=0.0001)
    st.write('Hasil dari volume cairan adalah=', volume_sampel)

    hitung_cu = st.button("Hitung kadar cemaran Cu")

    if hitung_cu:
        kadar_cemaran_cu = (c_terukur * v * FP) / (volume_sampel)
        st.write(f"Hasil perhitungan kadar cemaran Cu = {kadar_cemaran_cu} ppm")
if _name_ == '_main_':
    main()

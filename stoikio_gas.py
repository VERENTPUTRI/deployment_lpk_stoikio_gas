import streamlit as st
import extra_streamlit_components as stx

# judul aplikasi
st.title('✨Kalkulator Stoikiometri Gas✨')

# intro aplikasi
st.write('Aplikasi ini bertujuan untuk memudahkan dalam menghitung stoikiometri gas. Silakan pilih menu kalkulator untuk menghitung Massa Gas (gram), tekanan (P), volume (V), dan mol gas (n) kemudian ikuti perintah yang ditampilkan di layar.')
st.markdown('---')

tab = stx.tab_bar(data=[
    stx.TabBarItemData (id="Massa Gas", description="", title="Massa Gas"),
    stx.TabBarItemData (id="Tekanan", description="", title="Tekanan"),
    stx.TabBarItemData (id="Volume", description="", title="Volume"),
    stx.TabBarItemData (id="Mol Gas", description="", title="Mol Gas"),
])

# konstanta gas
R = 0.0821  # L.atm/mol.K

# menghitung massa gas 
if tab=="Massa Gas":
    gas = st.text_input('Masukkan nama gas (_Jika tidak ada, isi dengan variabel. Contoh : A_)')
    mol_gas = st.number_input('Masukkan jumlah mol gas (mol)', min_value=0.0)
    massa_molar = st.number_input('Masukkan massa molar gas (g/mol)', min_value=0.0)
    tombol = st.button('Hitung')
    if tombol:
        massa_gas = mol_gas * massa_molar
        st.write('# Nilai Massa Gas Tersebut adalah')
        st.success(f'{massa_gas:.4f} gram {gas}')
        st.balloons()

# menghitung tekanan
elif tab=="Tekanan":
    gas = st.text_input('Masukkan nama gas (_Jika tidak ada, isi dengan variabel. Contoh : A_)')
    mol_gas = st.number_input('Masukkan jumlah mol gas (mol)', min_value=0.0)
    input_suhu = st.number_input('Masukkan suhu gas', min_value=0.0)
    suhu = st.selectbox('Pilih satuan suhu', ('°C', 'Kelvin'))
    if suhu=='°C':
        konversi_suhu= input_suhu + 273
    else:
        konversi_suhu = input_suhu
    volume = st.number_input('Masukkan volume gas (L)', min_value=0.0)
    tombol = st.button('Hitung')
    if tombol:
        st.write('### Nilai Tekanan Gas Tersebut adalah')
        tekanan_gas = (mol_gas * R * konversi_suhu) / volume
        st.success(f'{tekanan_gas:.2f} atm {gas}')
        st.balloons()

# menghitung volume
elif tab=="Volume":
    gas = st.text_input('Masukkan nama gas (_Jika tidak ada, isi dengan variabel. Contoh : A_)')
    mol_gas = st.number_input('Masukkan jumlah mol gas (mol)', min_value=0.0)
    input_suhu = st.number_input('Masukkan suhu gas', min_value=0.0)
    suhu = st.selectbox('Pilih satuan suhu', ('°C', 'Kelvin'))
    if suhu=='°C':
        konversi_suhu= input_suhu + 273
    else:
        konversi_suhu = input_suhu
    tekanan = st.number_input('Masukkan tekanan gas (atm)', min_value=0.0)
    tombol = st.button('Hitung')
    if tombol:
        st.write('### Nilai Volume Gas Tersebut adalah')
        volume_gas = (mol_gas * R * konversi_suhu) / tekanan
        st.success(f'{volume_gas:.4f} L {gas}')
    if tombol:
        st.write('### Nilai Volume Gas pada STP adalah')
        volume_stp = (mol_gas * R * 273.0) / 1
        st.success(f'{volume_stp:.2f} L {gas}')
        st.write('Kondisi STP berada pada Suhu 273 K dan Tekanan 1 atm')
        st.balloons()
        
# menghitung mol gas        
elif tab=="Mol Gas":
    gas = st.text_input('Masukkan nama gas (_Jika tidak ada, isi dengan variabel. Contoh : A_)')
    tekanan = st.number_input('Masukkan tekanan (atm)', min_value=0.0)
    input_suhu = st.number_input('Masukkan suhu gas', min_value=0.0)
    suhu = st.selectbox('Pilih satuan suhu', ('°C', 'Kelvin'))
    if suhu=='°C':
        konversi_suhu= input_suhu + 273
    else:
        konversi_suhu = input_suhu
    volume = st.number_input('Masukkan volume gas (L)', min_value=0.0)
    tombol = st.button('Hitung')
    if tombol:
        st.write('### Nilai Mol Gas Tersebut adalah')
        mol_gas = (tekanan * volume) / (R * konversi_suhu)
        st.success(f'{mol_gas:.2f} mol {gas}')
        st.balloons()
        
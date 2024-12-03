# Meminta jumlah pasien
jumlah_pasien = int(input("Masukkan jumlah pasien: "))

# List untuk menyimpan data nama pasien, kadar gula puasa, dan kadar gula setelah makan
nama_pasien = []
kadar_gula_puasa = []
kadar_gula_setelah_makan = []

# Mengumpulkan data dari setiap pasien
for i in range(jumlah_pasien):
    # Input nama pasien
    nama = input(f"Masukkan nama pasien ke-{i+1}: ")
    nama_pasien.append(nama)
    
    # Input kadar gula darah puasa
    gula_puasa = float(input(f"Masukkan kadar gula puasa pasien {nama}: "))
    kadar_gula_puasa.append(gula_puasa)
    
    # Input kadar gula darah setelah makan
    gula_setelah_makan = float(input(f"Masukkan kadar gula setelah makan pasien {nama}: "))
    kadar_gula_setelah_makan.append(gula_setelah_makan)

# Menampilkan data yang telah dimasukkan dan kondisi pasien
print("\nData Pasien dan Kadar Gula Darah:")
for i in range(jumlah_pasien):
    kondisi_puasa = "Normal" if kadar_gula_puasa[i] <= 100 else "Berisiko"
    kondisi_setelah_makan = "Normal" if kadar_gula_setelah_makan[i] <= 140 else "Berisiko"
    
    print(f"{nama_pasien[i]}: Gula Puasa = {kadar_gula_puasa[i]} mg/dL ({kondisi_puasa}), Gula Setelah Makan = {kadar_gula_setelah_makan[i]} mg/dL ({kondisi_setelah_makan})")

# Menghitung rata-rata kadar gula puasa dan kadar gula setelah makan
rata_rata_gula_puasa = sum(kadar_gula_puasa) / jumlah_pasien
rata_rata_gula_setelah_makan = sum(kadar_gula_setelah_makan) / jumlah_pasien

# Menampilkan rata-rata
print(f"\nRata-rata kadar gula puasa: {rata_rata_gula_puasa:.2f} mg/dL")
print(f"Rata-rata kadar gula setelah makan: {rata_rata_gula_setelah_makan:.2f} mg/dL")

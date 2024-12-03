jumlah_pasien = int(input("Masukkan jumlah pasien: "))

nama_pasien = []
detak_jantung = []

for i in range(jumlah_pasien):
    nama = input(f"Masukkan nama pasien ke-{i+1}: ")
    detak = float(input(f"Masukkan detak jantung pasien {nama}: "))
    nama_pasien.append(nama)
    detak_jantung.append(detak)

ambang_batas = 120
total_detak = sum(detak_jantung)
rata_rata_detak_jantung = total_detak / jumlah_pasien

print("\nData Detak Jantung Pasien:")
for i in range(jumlah_pasien):
    print(f"{nama_pasien[i]}: {detak_jantung[i]} bpm")

pasien_di_atas_ambang = [nama_pasien[i] for i in range(jumlah_pasien) if detak_jantung[i] > ambang_batas]

print("\nPasien dengan detak jantung di atas ambang batas:")
for pasien in pasien_di_atas_ambang:
    print(pasien)

print(f"\nRata-rata detak jantung pasien: {rata_rata_detak_jantung:.2f} bpm")

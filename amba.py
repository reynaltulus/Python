
count = 0
while count < 3:
    nama = input(f"Masukkan Nama ke-{count+1}: ")
    sistolik = float(input("Masukkan tekanan darah sistolik: "))
    diastolik = float(input("Masukkan tekanan darah diastolik: "))
    denyut_nadi = float(input("Masukkan denyut nadi: "))

    
    if sistolik > 180 and diastolik > 120:
        kondisi = "Rekomendasikan pasien untuk segera mencari bantuan medis karena ini merupakan krisis hipertensi."
    else:
        if sistolik > 140 and diastolik > 90:
            kondisi = "Sarankan untuk konsultasi dengan dokter mengenai hipertensi."
        elif 120 <= sistolik <= 139 and 80 <= diastolik <= 89:
            kondisi = "Pasien berada dalam kategori prehipertensi."
            
            if denyut_nadi > 100:
                kondisi += " Sarankan untuk memeriksa kondisi kesehatan jantung."
            elif denyut_nadi < 60:
                kondisi += " Sarankan untuk memeriksa apakah ada gejala lain yang mengiringi bradikardia."
            else:
                kondisi += " Denyut nadi mereka normal."
        else:
            kondisi = "Tekanan darah normal."
            
    print(f"Nama: {nama}, Sistolik: {sistolik}, Diastolik: {diastolik}, Denyut Nadi: {denyut_nadi}, Kondisi: {kondisi}")
    print()  
    
    
    count += 1

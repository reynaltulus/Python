kondisi = ""
retry = 0

while retry < 5:
    bb = float(input("Masukkan berat badan: "))
    
    if bb < 18.5:
        kondisi = "underweight"
    elif 18.5 <= bb < 25:
        kondisi = "Normal weight"
    elif 25 <= bb < 30:
        kondisi = "overweight"
    else:
        kondisi = "obesitas"

    tb = int(input("Masukkan tinggi badan: "))
    
    if tb < 150:
        kondisi = "underheight"
    elif 150 <= tb < 170:
        kondisi = "normalheight"
    else:
        kondisi = "tinggi kamu wadidaw"
    
    print(f"Hasil Periksa bb: {kondisi}","hasil periksa tb:{kondisi}")
    
    question_retry = input("Masih ingin diperiksa? y/Y untuk Ya dan n/N untuk Tidak: ")
    if question_retry.lower() == 'y':
        retry += 1
        kondisi = ""
    else:
        break

print("Program selesai.")

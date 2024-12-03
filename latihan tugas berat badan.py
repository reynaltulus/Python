retry = 0

while retry < 3:
    bb = float(input("Masukkan berat badan: "))
    
    # Kondisi untuk berat badan
    if bb < 18.5:
        kondisi_bb = "underweight"
    elif 18.5 <= bb < 25:
        kondisi_bb = "Normal weight"
    elif 25 <= bb < 30:
        kondisi_bb = "overweight"
    else:
        kondisi_bb = "obesitas"

    tb = int(input("Masukkan tinggi badan: "))
    
    # Kondisi untuk tinggi badan
    if tb < 150:
        kondisi_tb = "underheight"
    elif 150 <= tb < 170:
        kondisi_tb = "normalheight"
    else:
        kondisi_tb = "tinggi banget cak"
    
    print(f"berat badan kamu: {kondisi_bb}, Tinggi Badan kamu: {kondisi_tb}")
    
    question_retry = input("Masih ingin mengecek ganteng ? y/Y untuk Ya dan n/N untuk Tidak: ")
    if question_retry.lower() == 'y':
        retry += 1
    else:
        break

print("Program selesai.")

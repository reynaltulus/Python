
kondisi= ""
retry = 0
while retry <5:
   bb = float(input("Masukkan masukkan berat badan: "))
    if 18.5 < bb:
        kondisi = ("underweight")
    else :
        if 18.5 bb <25:
            kondisi = ("Normal weight")
        elif 25 < bb <30:
            kondisi = ("overweight")
        else  :
            if bb >30:
            kondisi = ("obesitas")
    tb = int(input("Masukkan masukkan tinggi badan : ")) 
    if tb < 150 :
        kondisi = ("underheight")
    elif 150 < tb < 170  :
        kondisi = ("normalheight")
    else :
        kondisi = ("tinggi kamu wadidaw")
    
    print(f"Hasil bb : {kondisi}","hasil tb :{kondisi}")
    question_retry= input("Masih ingin diperiksa ? y/Y untuk Ya dan n/N untuk Tidak ")
    if question_retry.lower() in ['y'] :
        retry  +=1 
        kondisi = ""
    else :
        retry = 5
        kondisi = ""

    
        
    
        
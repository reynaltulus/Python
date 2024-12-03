nilai = int(input("masukkan nilai rapormu ambalang:"))
perilaku =input("perilaku kamu:")

if nilai>=80 and perilaku == 'baik':
    print("selamat!anda mendapat nilai A dan telah berkelakuan baik")
    print("pertahankan!")
elif nilai>=80 and perilaku != 'baik':
    print("kamu mendapatkan nilai A,tetapi perilaku anda kurang baik")
    print("perbaiki lagi ya!")
else:
    print("goblok mendingkerja joget bareng sadbor ")
    print("alah cuih jijik" )
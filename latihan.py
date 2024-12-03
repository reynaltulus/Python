def menghitung_rata2(jml_mhs):
    total = 0;

    for i in range (jml_mhs):
        nilai_mhs = float(input("masukkan nilai mahasiswa ke {i+1} : "))
        total += nilai_mhs

    return total/jml_mhs

jml = int(input("masukkan jumlah mahasiswa:"))
print(f"hasil rata2 dari {jml} org mahasiswa adalah (menghitung_rata2 {jml})")
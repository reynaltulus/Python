data_panen = {
    "lokasi1": {
        "nama_lokasi": "Kebun A",
        "hasil_panen": {"padi": 1200, "jagung": 800, "kedelai": 500},
    },
    "lokasi2": {
        "nama_lokasi": "Kebun B",
        "hasil_panen": {"padi": 1500, "jagung": 900, "kedelai": 450},
    },
    "lokasi3": {
        "nama_lokasi": "Kebun C",
        "hasil_panen": {"padi": 1100, "jagung": 750, "kedelai": 600},
    },
    "lokasi4": {
        "nama_lokasi": "Kebun D",
        "hasil_panen": {"padi": 1300, "jagung": 850, "kedelai": 550},
    },
    "lokasi5": {
        "nama_lokasi": "Kebun E",
        "hasil_panen": {"padi": 1400, "jagung": 950, "kedelai": 480},
    },
}


def panen_list(data):
    print(" ======== Nomor 1 ===========")
    for value in data.values():
        print(f"Lokasi panenkugi {value['nama_lokasi']}\nHasil panen\nJagung {value['hasil_panen']['jagung']}\nPadi {value['hasil_panen']['padi']}\nKedelai {value['hasil_panen']['kedelai']}\n")
    
    print("\n ======== Nomor 2 ===========")
    lokasi2 = data.get("lokasi2")
    if lokasi2:
        print(f"Lokasi {lokasi2['nama_lokasi']}\nHasil panen\nJagung {lokasi2['hasil_panen']['jagung']}\n")
    
    print("\n ======== Nomor 3 ===========")
    lokasi3 = data.get("lokasi3")
    if lokasi3:
        print(f"Nama Lokasi dari lokasi3 adalah {lokasi3['nama_lokasi']}\n")
    
    print(" ======== Nomor 4 ===========")
    rice_fields_sum = sum(val["hasil_panen"]["padi"] for val in data.values())
    soybean_fields_sum = sum(val["hasil_panen"]["kedelai"] for val in data.values())
    print(f"Hasil panen Padi : {rice_fields_sum} , Kedelai : {soybean_fields_sum}")
    
    print("\n ======== Nomor 5 ===========")
    for value in data.values():
        print(f"Lokasi {value['nama_lokasi']}\nPadi: {value['hasil_panen']['padi']}\nKedelai: {value['hasil_panen']['kedelai']}\nJagung: {value['hasil_panen']['jagung']}\n")
    
    print("\n\n\n ======== Nomor 6 ===========")
    for key, val in data.items():
        if val['hasil_panen']['padi'] > 1300 or val['hasil_panen']['jagung'] > 800:
            print(f"Lokasi {key} memerlukan perhatian khusus")
        else:
            print(f"Lokasi {key} dalam kondisi baik")


panen_list(data_panen)
print('aku sayang rokok')
print('ghalit gercep kalo ke cewe')

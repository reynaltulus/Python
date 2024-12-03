
data_sampah = {
    "organik": {"jumlah": 120, "lokasi": "TPA Organik"},
    "anorganik": {"jumlah": 250, "lokasi": "Pusat Daur Ulang"},
    "B3": {"jumlah": 60, "lokasi": "Tempat Pengelolaan B3"}
}

print("Jumlah sampah anorganik:", data_sampah["anorganik"]["jumlah"], "kg")
print("Lokasi pembuangan sampah B3:", data_sampah["B3"]["lokasi"])

data_sampah["elektronik"] = {"jumlah": 40, "lokasi": "Pusat Pengelolaan Elektronik"}

data_sampah["organik"]["jumlah"] = 130

print("\nDictionary setelah pembaruan:", data_sampah)


for jenis_sampah, info in data_sampah.items():
    if info["jumlah"] > 100:
        print(f"Pengelolaan intensif diperlukan untuk {jenis_sampah}")
    else:
        print(f"{jenis_sampah} dalam batas aman")

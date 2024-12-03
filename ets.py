option = int(
    input(
        "Masukkan Opsi mana yang akan dipilih ( C ke F : 1 , F ke C : 2 atau C ke K :3   )"
    )
)
temp = float(input("Masukkan temperature : "))
result = 0
temp_name = []
if option in [1, 2, 3]:
    if option == 1:
        result = temp * 9 / 5 + 32
        temp_name.extend(["Celcius", "Farenheit"])
    elif option == 2:
        result = (temp - 32) * 5 / 9
        temp_name.extend(["Farenheit", "Celcius"])
    else:
        result = temp + 273.15
        temp_name.extend(["Celcius", "Kelvin"])
else:
    print("Opsi salah")

print(
    f"Temperature dari {temp_name[0]} di konvert menjadi {temp_name[1]} adalah {result}"
)
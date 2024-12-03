def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    c = fahrenheit_to_celsius(f)
    return celsius_to_kelvin(c)

def kelvin_to_fahrenheit(k):
    c = kelvin_to_celsius(k)
    return celsius_to_fahrenheit(c)

def main():
    print("Pilih konversi suhu:")
    print("1. Celsius ke Fahrenheit")
    print("2. Fahrenheit ke Celsius")
    print("3. Celsius ke Kelvin")
    print("4. Kelvin ke Celsius")
    print("5. Fahrenheit ke Kelvin")
    print("6. Kelvin ke Fahrenheit")
    
    choice = input("Masukkan pilihan (1-6): ")
    suhu = float(input("Masukkan suhu: "))

    if choice == '1':
        result = celsius_to_fahrenheit(suhu)
        print(f"{suhu} °C = {result} °F")
    elif choice == '2':
        result = fahrenheit_to_celsius(suhu)
        print(f"{suhu} °F = {result} °C")
    elif choice == '3':
        result = celsius_to_kelvin(suhu)
        print(f"{suhu} °C = {result} K")
    elif choice == '4':
        result = kelvin_to_celsius(suhu)
        print(f"{suhu} K = {result} °C")
    elif choice == '5':
        result = fahrenheit_to_kelvin(suhu)
        print(f"{suhu} °F = {result} K")
    elif choice == '6':
        result = kelvin_to_fahrenheit(suhu)
        print(f"{suhu} K = {result} °F")
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    c = fahrenheit_to_celsius(f)
    return celsius_to_kelvin(c)

def kelvin_to_fahrenheit(k):
    c = kelvin_to_celsius(k)
    return celsius_to_fahrenheit(c)

def main():
    print("Pilih konversi suhu:")
    print("1. Celsius ke Fahrenheit")
    print("2. Fahrenheit ke Celsius")
    print("3. Celsius ke Kelvin")
    print("4. Kelvin ke Celsius")
    print("5. Fahrenheit ke Kelvin")
    print("6. Kelvin ke Fahrenheit")
    
    choice = input("Masukkan pilihan (1-6): ")
    suhu = float(input("Masukkan suhu: "))

    if choice == '1':
        result = celsius_to_fahrenheit(suhu)
        print(f"{suhu} °C = {result} °F")
    elif choice == '2':
        result = fahrenheit_to_celsius(suhu)
        print(f"{suhu} °F = {result} °C")
    elif choice == '3':
        result = celsius_to_kelvin(suhu)
        print(f"{suhu} °C = {result} K")
    elif choice == '4':
        result = kelvin_to_celsius(suhu)
        print(f"{suhu} K = {result} °C")
    elif choice == '5':
        result = fahrenheit_to_kelvin(suhu)
        print(f"{suhu} °F = {result} K")
    elif choice == '6':
        result = kelvin_to_fahrenheit(suhu)
        print(f"{suhu} K = {result} °F")
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()

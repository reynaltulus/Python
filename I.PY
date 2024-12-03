import time
import Adafruit_DHT
import RPi.GPIO as GPIO

# Konfigurasi GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Pin GPIO untuk buzzer
BUZZER_KERAS = 18  # Buzzer dengan suara keras (>= 38°C)
BUZZER_SEDANG = 23  # Buzzer dengan suara sedang (18°C <= suhu < 38°C)
BUZZER_OFF = 24  # Buzzer tidak menyala jika suhu < 18°C

# Pin DHT11
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 17  # Pin data untuk sensor DHT11

# Setup GPIO untuk Buzzer
GPIO.setup(BUZZER_KERAS, GPIO.OUT)
GPIO.setup(BUZZER_SEDANG, GPIO.OUT)
GPIO.setup(BUZZER_OFF, GPIO.OUT)

try:
    while True:
        # Membaca data dari sensor DHT11
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

        # Jika pembacaan berhasil, lanjutkan
        if humidity is not None and temperature is not None:
            # Reset semua buzzer sebelum menentukan kondisi
            GPIO.output(BUZZER_KERAS, GPIO.LOW)
            GPIO.output(BUZZER_SEDANG, GPIO.LOW)
            GPIO.output(BUZZER_OFF, GPIO.LOW)

            # Kondisi berdasarkan suhu
            if temperature >= 38:
                kondisi = "sangat panas"
                GPIO.output(BUZZER_KERAS, GPIO.HIGH)  # Buzzer keras menyala
            elif 18 <= temperature < 38:
                kondisi = "suhu sedang"
                GPIO.output(BUZZER_SEDANG, GPIO.HIGH)  # Buzzer sedang menyala
            else:
                kondisi = "suhu dingin"
                # Buzzer tidak menyala untuk suhu di bawah 18°C
                GPIO.output(BUZZER_OFF, GPIO.LOW)

            # Output kondisi ke terminal
            print(f"suhu: {temperature} derajat celcius - kondisi {kondisi}")
        else:
            print("Gagal membaca data dari sensor DHT11")

        # Tunggu 5 detik sebelum iterasi berikutnya
        time.sleep(5)

except KeyboardInterrupt:
    print("Program dihentikan oleh pengguna")

finally:
    GPIO.cleanup()  # Pastikan GPIO dibersihkan saat program selesai

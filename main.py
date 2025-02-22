import time
import os
import speedtest
import socket
import requests
import webbrowser
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz
from termcolor import colored

def clear_screen():
    # Mengecek sistem operasi
    if os.name == 'nt':  # Jika Windows
        os.system('cls')
    else:  # Jika Linux atau MacOS
        os.system('clear')

#=====================================================================================================================
# menampilkan detail informasi user
# Fungsi untuk mendapatkan lokasi pengguna menggunakan ip-api.com API
def get_location():
    # Menggunakan API ip-api.com untuk mendapatkan koordinat berdasarkan alamat IP
    try:
        response = requests.get("http://ip-api.com/json/")  # Layanan geocoding gratis
        if response.status_code == 200:
            data = response.json()
            lat = data.get("lat", 0)  # Mendapatkan latitude
            lon = data.get("lon", 0)  # Mendapatkan longitude
            city = data.get("city", "Tidak Diketahui")  # Nama kota
            country = data.get("country", "Tidak Diketahui")  # Nama negara
            return lat, lon, city, country
        else:
            print("Gagal mengambil data geolokasi.")
            return 0, 0, "Tidak Diketahui", "Tidak Diketahui"
    except requests.exceptions.RequestException as e:
        print(f"Terjadi kesalahan koneksi: {e}")
        return 0, 0, "Tidak Diketahui", "Tidak Diketahui"

# Fungsi untuk mendapatkan zona waktu berdasarkan koordinat
def get_timezone(lat, lon):
    tf = TimezoneFinder()
    result = tf.timezone_at(lng=lon, lat=lat)
    return result

# Fungsi untuk mendapatkan waktu saat ini dalam zona waktu lokal
def get_local_time(timezone_str):
    tz = pytz.timezone(timezone_str)
    local_time = datetime.now(tz)
    return local_time.strftime('%H:%M:%S')

# Fungsi untuk menampilkan informasi dalam satu baris horizontal
def display_info():
    lat, lon, city, country = get_location()  # Mendapatkan koordinat lokasi
    if lat == 0 and lon == 0:
        print("Gagal mengambil lokasi.")
        return

    timezone_str = get_timezone(lat, lon)  # Mendapatkan zona waktu berdasarkan lokasi
    local_time = get_local_time(timezone_str)  # Mendapatkan waktu lokal berdasarkan zona waktu

    # Menampilkan semua informasi dalam satu baris horizontal
    print(f"Lokasi: {city}, {country} | Koordinat: {lat}, {lon} | Zona Waktu: {timezone_str} | Waktu Lokal: {local_time}")


#=====================================================================================================================

#Tools 1: Scan your ip
def get_local_ip():
    # Mendapatkan alamat IP lokal dengan menghubungkan ke server luar
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # Menghubungkan ke server luar untuk mendapatkan IP
        s.connect(('10.254.254.254', 1))
        local_ip = s.getsockname()[0]
    except Exception:
        local_ip = 'IP tidak ditemukan'
    finally:
        s.close()
    
    return local_ip

#Tools 2: Track IP Address
import requests

# Fungsi untuk melacak alamat IP
def track_ip(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    data = response.json()

    # Menampilkan informasi IP yang ditemukan
    if data.get('status') == 'fail':
        print("Gagal melacak alamat IP. Coba alamat IP yang valid.")
    else:
        print("Informasi IP:")
        print(f"Alamat IP: {data.get('query')}")
        print(f"Lokasi: {data.get('city')}, {data.get('regionName')}, {data.get('country')}")
        print(f"ISP: {data.get('isp')}")
        print(f"Organisasi: {data.get('org')}")
        print(f"Geo: {data.get('lat')}, {data.get('lon')}")
        print("-" * 50)

# Fungsi untuk meminta input alamat IP dari pengguna
def get_ip_from_user():
    print("")
    ip_address = input("Enter the IP address you want to track : ")
        
    track_ip(ip_address)


# Tools 3: Test kecepatan internet
def test_speed():
    st = speedtest.Speedtest()

    # Mendapatkan daftar server yang tersedia
    servers = st.get_servers()

    # Periksa apakah servers memiliki data
    if servers:
        # Menemukan server terbaik (bisa juga memilih server berdasarkan kriteria tertentu)
        best_server = None
        for server_list in servers.values():  # Iterasi melalui server yang ada dalam dictionary
            best_server = server_list[0]  # Pilih server pertama (bisa disesuaikan)

        if best_server:
            st.get_best_server([best_server])  # Pilih server terbaik

        # Mengukur kecepatan download
        download_speed = st.download() / 1_000_000  # Mengubah kecepatan ke Mbps

        # Mengukur kecepatan upload
        upload_speed = st.upload() / 1_000_000  # Mengubah kecepatan ke Mbps

        # Mengukur ping
        ping = st.results.ping

        # Menampilkan hasil
        print(f"\nDownload Speed: {download_speed:.2f} Mbps")
        print(f"Upload Speed: {upload_speed:.2f} Mbps")
        print(f"Ping: {ping} ms")
    else:
        print("There are no servers available for testing.")


clear_screen()
# Teks yang ingin ditampilkan dengan warna
text = colored('just', 'green') + colored('Fun', 'yellow', attrs=['bold']) + colored(' Tools v1', 'white') + colored(' by Danvastra', 'red') 
print(""" 
    _              _    _____              
   (_) _   _  ___ | |_ |  ___|_   _  _ __  
   | || | | |/ __|| __|| |_  | | | || '_ \ 
   | || |_| |\__ \| |_ |  _| | |_| || | | |
  _/ | \__,_||___/ \__||_|    \__,_||_| |_|v.1
 |__/                                      
""")

# Ukuran kotak (menambahkan padding agar teks tidak terlalu rapat dengan garis)
padding = 1  # Mengurangi padding
width = len(text) + padding * 2  # Menambahkan padding kiri dan kanan

# Mencetak garis atas dengan panjang yang dikurangi
print('+' + '-' * (width - 2) + '+')

# Mencetak baris dengan teks
print('|' + ' ' * padding + text + ' ' * padding + '|')

# Mencetak garis bawah dengan panjang yang dikurangi
print('+' + '-' * (width - 2) + '+')

# User input token terlebih dahulu
text2 = colored('Link Token : ', 'green') + colored('https://bit.ly/justFunToken', 'yellow', attrs=['bold'])
print(text2)

# Perulangan untuk meminta input token sampai valid
tokenValid = str(input('Input Token : '))

# Simulasi loading palsu untuk memverifikasi token
loading_text = colored("Verifying the token", 'yellow', attrs=['bold'])  # Menggunakan warna hijau
print(loading_text, end="")
for _ in range(3):  # Menambahkan titik selama 5 detik
    print(".", end="", flush=True)
    time.sleep(1)  # Menunggu 1 detik
print()  # Menambahkan baris baru setelah loading

def loadingData():
    # loading data
    loading = colored("Loading Data", 'green')  # Menggunakan warna hijau
    print(loading, end="")
    for _ in range(3):  # Menambahkan titik selama 5 detik
        print(".", end="", flush=True)
        time.sleep(1)  # Menunggu 1 detik
    print()  # Menambahkan baris baru setelah loading

def menuTools():
    # Validasi token
    if tokenValid == 'JBDaojdiopjdkdxioHAIdJKSdaknf':
        validToken = colored('Your Token is Valid!', 'green')
        print(validToken)

        # Menunggu sebentar sebelum membersihkan layar agar pesan terlihat
        time.sleep(1)
        clear_screen()

        # justFun Tools Version 1
        # Ukuran kotak (menambahkan padding agar teks tidak terlalu rapat dengan garis)
        padding = 2
        width = len(text) + padding * 2  # Menambahkan padding kiri dan kanan
        # Mencetak garis atas
        print('+' + '-' * (width - 2) + '+')
        # Mencetak baris dengan teks
        print('|' + ' ' * padding + text + ' ' * padding + '|')
        # Mencetak garis bawah
        print('+' + '-' * (width - 2) + '+')

        display_info()
        # User Memilih tools!
        selectTools = colored('[Please Select Tools]', 'cyan')
        tools1 = colored('[1]', 'yellow', attrs=['bold']) + colored(' Scan ip Address', 'green')
        tools2 = colored('[2]', 'yellow', attrs=['bold']) + colored(' Track IP Address', 'green')
        tools3 = colored('[3]', 'yellow', attrs=['bold']) + colored(' Test Speed Internet', 'green')
        support = colored('[4]', 'yellow', attrs=['bold']) + colored(' Support Author', 'green')
        exit = colored('[5]', 'yellow', attrs=['bold']) + colored(' Close The Program!', 'green')
        print(tools1)
        print(tools2)
        print(tools3)
        print(support)
        print(exit)

        chooseTools = int(input('Choose your tools! (ex.1/2/3/4) : '))
        if chooseTools == 1:
            loadingData()

            print('')
            ip = get_local_ip()
            print(f"Your local IP address: {ip}")
            print('')
            lanjut = input("Return to main menu or exit? (y/n): ").lower()
            if lanjut == 'n':
                print("Exit the program...")
                return False  # Keluar dari menuTools
            elif lanjut != 'y':
                print("Invalid choice, exit the program.")
                return False  # Keluar dari menuTools
        elif chooseTools == 2:
            loadingData()
            get_ip_from_user()
            print('')
            lanjut = input("Return to main menu or exit? (y/n): ").lower()
            if lanjut == 'n':
                print("Exit the program...")
                return False  # Keluar dari menuTools
            elif lanjut != 'y':
                print("Invalid choice, exit the program.")
                return False  # Keluar dari menuTools
        elif chooseTools == 3:

            loadingData()

            test_speed()  # Jalankan test speed
            print("")
            lanjut = input("Return to main menu or exit? (y/n): ").lower()
            if lanjut == 'n':
                print("Exit the program...")
                return False  # Keluar dari menuTools
            elif lanjut != 'y':
                print("Invalid choice, exit the program.")

                return False  # Keluar dari menuTools
        elif chooseTools == 4:
            link = "https://saweria.co/dvstra5"
            print("")
            # Menunggu user tekan Enter untuk membuka link
            input("Tekan Enter untuk Donasi ke Author...")
            webbrowser.open(link)
            lanjut = input("Return to main menu or exit? (y/n): ").lower()
            if lanjut == 'n':
                print("Exit the program...")
                return False  # Keluar dari menuTools
            elif lanjut != 'y':
                print("Invalid choice, exit the program.")

            return False  # Keluar dari menuTools (keluar dari program)
        elif chooseTools == 5:
            print("Thanks for trying this tool!")
            return False  # Keluar dari menuTools (keluar dari program)
        else:
            print('An error has occurred!')
        return True  # Lanjutkan ke menuTools jika memilih kembali
    else:
        invalidToken = colored('Error! Invalid token. Try again.', 'red')
        print(invalidToken)
        return False  # Kembali ke input token jika token tidak valid

# Menjalankan menuTools hanya sekali
while True:
    if not menuTools():  # Jika menuTools mengembalikan False, keluar dari loop
        break

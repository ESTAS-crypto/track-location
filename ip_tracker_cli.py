"""
IP Location Tracker - Terminal/CLI Version
Melacak lokasi berdasarkan IP dan memberikan link Google Maps

⚠️  CATATAN PENTING:
Pelacakan IP hanya akurat sampai tingkat KOTA atau AREA ISP.
IP geolocation TIDAK BISA menentukan lokasi tepat seperti GPS.
Lokasi yang ditampilkan adalah perkiraan berdasarkan data ISP.
"""

import requests
import sys

def get_location_ipapi(ip_address):
    """Mendapatkan lokasi dari ip-api.com"""
    try:
        response = requests.get(
            f'http://ip-api.com/json/{ip_address}?fields=status,message,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,isp,org,as,query',
            timeout=10
        )
        data = response.json()
        if data.get('status') == 'success':
            return {
                'source': 'ip-api.com',
                'ip': data.get('query'),
                'country': data.get('country'),
                'country_code': data.get('countryCode'),
                'region': data.get('regionName'),
                'city': data.get('city'),
                'district': data.get('district', '-'),
                'zip': data.get('zip'),
                'lat': data.get('lat'),
                'lon': data.get('lon'),
                'timezone': data.get('timezone'),
                'isp': data.get('isp'),
                'org': data.get('org'),
                'as': data.get('as')
            }
    except:
        pass
    return None

def get_location_ipinfo(ip_address):
    """Mendapatkan lokasi dari ipinfo.io"""
    try:
        response = requests.get(
            f'https://ipinfo.io/{ip_address}/json',
            timeout=10
        )
        data = response.json()
        if 'loc' in data:
            lat, lon = data.get('loc', '0,0').split(',')
            return {
                'source': 'ipinfo.io',
                'ip': data.get('ip'),
                'country': data.get('country'),
                'country_code': data.get('country'),
                'region': data.get('region'),
                'city': data.get('city'),
                'district': '-',
                'zip': data.get('postal', '-'),
                'lat': float(lat),
                'lon': float(lon),
                'timezone': data.get('timezone'),
                'isp': data.get('org', '-'),
                'org': data.get('org', '-'),
                'as': '-'
            }
    except:
        pass
    return None

def get_location_ipwhois(ip_address):
    """Mendapatkan lokasi dari ipwhois.app"""
    try:
        response = requests.get(
            f'https://ipwhois.app/json/{ip_address}',
            timeout=10
        )
        data = response.json()
        if data.get('success', True):
            return {
                'source': 'ipwhois.app',
                'ip': data.get('ip'),
                'country': data.get('country'),
                'country_code': data.get('country_code'),
                'region': data.get('region'),
                'city': data.get('city'),
                'district': '-',
                'zip': data.get('postal', '-'),
                'lat': data.get('latitude'),
                'lon': data.get('longitude'),
                'timezone': data.get('timezone'),
                'isp': data.get('isp', '-'),
                'org': data.get('org', '-'),
                'as': data.get('asn', '-')
            }
    except:
        pass
    return None

def get_my_public_ip():
    """Dapatkan IP publik"""
    apis = [
        'https://api.ipify.org?format=json',
        'https://api.my-ip.io/ip.json',
        'https://ipinfo.io/ip'
    ]
    
    for api in apis:
        try:
            response = requests.get(api, timeout=5)
            if 'json' in api:
                data = response.json()
                return data.get('ip') or data.get('IP')
            else:
                return response.text.strip()
        except:
            continue
    return None

def print_separator():
    """Print garis pemisah"""
    print("=" * 65)

def print_warning_box():
    """Print kotak peringatan tentang akurasi"""
    print()
    print("┌─────────────────────────────────────────────────────────────────┐")
    print("│  ⚠️  PERINGATAN AKURASI                                         │")
    print("├─────────────────────────────────────────────────────────────────┤")
    print("│  Pelacakan IP HANYA akurat sampai tingkat KOTA atau AREA ISP.  │")
    print("│  Lokasi yang ditampilkan adalah perkiraan, BUKAN lokasi tepat. │")
    print("│  Untuk lokasi tepat, diperlukan GPS dari perangkat.            │")
    print("└─────────────────────────────────────────────────────────────────┘")
    print()

def main():
    try:
        print_separator()
        print("🌐  IP LOCATION TRACKER - Terminal Version")
        print("📍  Lacak lokasi IP dan dapatkan link Google Maps")
        print_separator()
        print_warning_box()
        
        while True:
            # Tampilkan menu
            print("Pilihan:")
            print("  1. Masukkan IP untuk dilacak")
            print("  2. Lacak IP saya sendiri")
            print("  3. Keluar")
            print()
            
            try:
                pilihan = input("Masukkan pilihan (1/2/3): ").strip()
            except (KeyboardInterrupt, EOFError):
                print("\n\n👋 Program dihentikan oleh pengguna.")
                sys.exit(0)
            
            print()
            
            if pilihan == "3":
                print("👋 Terima kasih telah menggunakan IP Location Tracker!")
                break
            
            elif pilihan == "1":
                try:
                    ip_address = input("Masukkan IP Address: ").strip()
                except (KeyboardInterrupt, EOFError):
                    print("\n\n👋 Program dihentikan oleh pengguna.")
                    sys.exit(0)
                
                if not ip_address:
                    print("❌ IP Address tidak boleh kosong!\n")
                    continue
                    
                print(f"\n🔍 Melacak IP: {ip_address}...")
                
            elif pilihan == "2":
                print("🔍 Mencari IP publik Anda...")
                ip_address = get_my_public_ip()
                
                if not ip_address:
                    print("❌ Gagal mendapatkan IP Anda. Cek koneksi internet.\n")
                    continue
                    
                print(f"✅ IP Anda terdeteksi: {ip_address}\n")
                print("🔍 Melacak lokasi...")
                
            else:
                print("❌ Pilihan tidak valid! Masukkan 1, 2, atau 3.\n")
                continue
            
            # Coba beberapa API untuk hasil terbaik
            print("   📡 Mencoba beberapa sumber data...")
            print()
            
            results = []
            
            # API 1: ip-api.com
            print("   ├─ Mengecek ip-api.com...", end=" ")
            result1 = get_location_ipapi(ip_address)
            if result1:
                results.append(result1)
                print("✓")
            else:
                print("✗")
            
            # API 2: ipinfo.io
            print("   ├─ Mengecek ipinfo.io...", end=" ")
            result2 = get_location_ipinfo(ip_address)
            if result2:
                results.append(result2)
                print("✓")
            else:
                print("✗")
            
            # API 3: ipwhois.app
            print("   └─ Mengecek ipwhois.app...", end=" ")
            result3 = get_location_ipwhois(ip_address)
            if result3:
                results.append(result3)
                print("✓")
            else:
                print("✗")
            
            print()
            
            if not results:
                print("❌ Gagal mendapatkan data lokasi dari semua sumber.")
                print("   IP mungkin tidak valid atau koneksi bermasalah.\n")
                continue
            
            # Gunakan hasil pertama yang berhasil
            location_data = results[0]
            
            # Ambil koordinat
            latitude = location_data.get('lat')
            longitude = location_data.get('lon')
            
            # Buat link Google Maps dengan zoom yang sesuai (zoom 12 = level kota)
            google_maps_link = f"https://www.google.com/maps?q={latitude},{longitude}&z=12"
            google_maps_search = f"https://www.google.com/maps/search/{location_data.get('city')},+{location_data.get('region')},+{location_data.get('country')}"
            
            # Tampilkan hasil
            print_separator()
            print("📍 HASIL PELACAKAN IP")
            print_separator()
            print()
            print(f"  🌐 IP Address    : {location_data.get('ip')}")
            print(f"  🏳️  Negara        : {location_data.get('country')} ({location_data.get('country_code')})")
            print(f"  📍 Wilayah       : {location_data.get('region')}")
            print(f"  🏙️  Kota          : {location_data.get('city')}")
            if location_data.get('district') and location_data.get('district') != '-':
                print(f"  🏘️  Distrik       : {location_data.get('district')}")
            print(f"  📮 Kode Pos      : {location_data.get('zip')}")
            print(f"  🌍 Koordinat     : {latitude}, {longitude}")
            print(f"  🕐 Timezone      : {location_data.get('timezone')}")
            print(f"  📡 ISP           : {location_data.get('isp')}")
            print(f"  🏢 Organisasi    : {location_data.get('org')}")
            print(f"  🔢 AS Number     : {location_data.get('as')}")
            print(f"  📊 Sumber Data   : {location_data.get('source')}")
            print()
            
            # Tampilkan perbandingan jika ada lebih dari satu hasil
            if len(results) > 1:
                print("  📋 Perbandingan dari sumber lain:")
                for i, res in enumerate(results[1:], 2):
                    print(f"     {i}. {res.get('source')}: {res.get('city')}, {res.get('region')}")
                print()
            
            print_separator()
            print("🗺️  LINK GOOGLE MAPS:")
            print()
            print(f"  Koordinat : {google_maps_link}")
            print(f"  Kota      : {google_maps_search}")
            print()
            print("  📌 Copy salah satu link di atas dan buka di browser")
            print_separator()
            print()
            print_warning_box()

    except (KeyboardInterrupt, EOFError):
        print("\n\n👋 Program dihentikan oleh pengguna.")
        sys.exit(0)

if __name__ == '__main__':
    main()

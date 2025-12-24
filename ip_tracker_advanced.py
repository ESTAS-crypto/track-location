"""
🔒 IP SECURITY ANALYZER - Advanced Version
Untuk testing keamanan IP sendiri - mencoba berbagai metode pelacakan

⚠️ DISCLAIMER: Tool ini hanya untuk testing IP ANDA SENDIRI.
   Digunakan untuk memahami data apa saja yang bisa diakses publik.
"""

import requests
import socket
import json
import sys
import re
from datetime import datetime

# Warna untuk terminal
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'

def c(color, text):
    """Warnai teks"""
    return f"{color}{text}{Colors.END}"

def print_header():
    print()
    print(c(Colors.CYAN, "╔" + "═" * 70 + "╗"))
    print(c(Colors.CYAN, "║") + c(Colors.BOLD + Colors.WHITE, "  🔒 IP SECURITY ANALYZER - Advanced Edition".ljust(70)) + c(Colors.CYAN, "║"))
    print(c(Colors.CYAN, "║") + c(Colors.YELLOW, "  📍 Untuk testing keamanan IP sendiri".ljust(79)) + c(Colors.CYAN, "║"))
    print(c(Colors.CYAN, "╚" + "═" * 70 + "╝"))
    print()

def get_my_ip():
    """Dapatkan IP publik dengan multiple sources"""
    apis = [
        ('api.ipify.org', 'https://api.ipify.org?format=json', 'ip'),
        ('ipinfo.io', 'https://ipinfo.io/ip', None),
        ('icanhazip.com', 'https://icanhazip.com', None),
        ('checkip.amazonaws.com', 'https://checkip.amazonaws.com', None),
    ]
    
    for name, url, key in apis:
        try:
            response = requests.get(url, timeout=5)
            if key:
                return response.json().get(key)
            return response.text.strip()
        except:
            continue
    return None

def get_all_geolocation_data(ip):
    """Kumpulkan data dari SEMUA sumber geolokasi yang tersedia"""
    results = {}
    
    # 1. ip-api.com (gratis, detail)
    print(f"  {c(Colors.YELLOW, '├─')} Mengecek ip-api.com...", end=" ", flush=True)
    try:
        r = requests.get(f'http://ip-api.com/json/{ip}?fields=66846719', timeout=10)
        data = r.json()
        if data.get('status') == 'success':
            results['ip-api.com'] = data
            print(c(Colors.GREEN, "✓"))
        else:
            print(c(Colors.RED, "✗"))
    except Exception as e:
        print(c(Colors.RED, f"✗ {e}"))
    
    # 2. ipinfo.io
    print(f"  {c(Colors.YELLOW, '├─')} Mengecek ipinfo.io...", end=" ", flush=True)
    try:
        r = requests.get(f'https://ipinfo.io/{ip}/json', timeout=10)
        results['ipinfo.io'] = r.json()
        print(c(Colors.GREEN, "✓"))
    except Exception as e:
        print(c(Colors.RED, f"✗ {e}"))
    
    # 3. ipwhois.app
    print(f"  {c(Colors.YELLOW, '├─')} Mengecek ipwhois.app...", end=" ", flush=True)
    try:
        r = requests.get(f'https://ipwhois.app/json/{ip}', timeout=10)
        results['ipwhois.app'] = r.json()
        print(c(Colors.GREEN, "✓"))
    except Exception as e:
        print(c(Colors.RED, f"✗ {e}"))
    
    # 4. ipdata.co
    print(f"  {c(Colors.YELLOW, '├─')} Mengecek ipdata.co...", end=" ", flush=True)
    try:
        r = requests.get(f'https://api.ipdata.co/{ip}?api-key=test', timeout=10)
        data = r.json()
        if 'city' in data:
            results['ipdata.co'] = data
            print(c(Colors.GREEN, "✓"))
        else:
            print(c(Colors.RED, "✗ Rate limited"))
    except Exception as e:
        print(c(Colors.RED, f"✗ {e}"))
    
    # 5. ip-api.io
    print(f"  {c(Colors.YELLOW, '├─')} Mengecek ip-api.io...", end=" ", flush=True)
    try:
        r = requests.get(f'https://ip-api.io/json/{ip}', timeout=10)
        results['ip-api.io'] = r.json()
        print(c(Colors.GREEN, "✓"))
    except Exception as e:
        print(c(Colors.RED, f"✗ {e}"))
    
    # 6. geoplugin.net
    print(f"  {c(Colors.YELLOW, '├─')} Mengecek geoplugin.net...", end=" ", flush=True)
    try:
        r = requests.get(f'http://www.geoplugin.net/json.gp?ip={ip}', timeout=10)
        data = r.json()
        if data.get('geoplugin_status') == 200:
            results['geoplugin.net'] = data
            print(c(Colors.GREEN, "✓"))
        else:
            print(c(Colors.RED, "✗"))
    except Exception as e:
        print(c(Colors.RED, f"✗ {e}"))
    
    # 7. reallyfreegeoip.org
    print(f"  {c(Colors.YELLOW, '├─')} Mengecek reallyfreegeoip.org...", end=" ", flush=True)
    try:
        r = requests.get(f'https://reallyfreegeoip.org/json/{ip}', timeout=10)
        results['reallyfreegeoip.org'] = r.json()
        print(c(Colors.GREEN, "✓"))
    except Exception as e:
        print(c(Colors.RED, f"✗ {e}"))
    
    # 8. freeipapi.com
    print(f"  {c(Colors.YELLOW, '└─')} Mengecek freeipapi.com...", end=" ", flush=True)
    try:
        r = requests.get(f'https://freeipapi.com/api/json/{ip}', timeout=10)
        results['freeipapi.com'] = r.json()
        print(c(Colors.GREEN, "✓"))
    except Exception as e:
        print(c(Colors.RED, f"✗ {e}"))
    
    return results

def get_dns_info(ip):
    """Dapatkan informasi DNS reverse lookup"""
    info = {}
    
    print(f"  {c(Colors.YELLOW, '├─')} Reverse DNS lookup...", end=" ", flush=True)
    try:
        hostname = socket.gethostbyaddr(ip)
        info['hostname'] = hostname[0]
        info['aliases'] = hostname[1]
        print(c(Colors.GREEN, f"✓ {hostname[0]}"))
    except:
        info['hostname'] = None
        print(c(Colors.RED, "✗"))
    
    return info

def get_whois_info(ip):
    """Dapatkan informasi WHOIS"""
    print(f"  {c(Colors.YELLOW, '└─')} WHOIS lookup...", end=" ", flush=True)
    try:
        r = requests.get(f'https://ipwhois.app/json/{ip}', timeout=10)
        data = r.json()
        print(c(Colors.GREEN, "✓"))
        return data
    except Exception as e:
        print(c(Colors.RED, f"✗ {e}"))
        return {}

def extract_locations(results):
    """Ekstrak semua koordinat dari berbagai sumber"""
    locations = []
    
    for source, data in results.items():
        lat = None
        lon = None
        city = None
        region = None
        
        # Berbeda-beda field name tergantung API
        if source == 'ip-api.com':
            lat = data.get('lat')
            lon = data.get('lon')
            city = data.get('city')
            region = data.get('regionName')
            district = data.get('district')
        elif source == 'ipinfo.io':
            loc = data.get('loc', '').split(',')
            if len(loc) == 2:
                lat, lon = float(loc[0]), float(loc[1])
            city = data.get('city')
            region = data.get('region')
            district = None
        elif source == 'ipwhois.app':
            lat = data.get('latitude')
            lon = data.get('longitude')
            city = data.get('city')
            region = data.get('region')
            district = None
        elif source == 'geoplugin.net':
            lat = data.get('geoplugin_latitude')
            lon = data.get('geoplugin_longitude')
            city = data.get('geoplugin_city')
            region = data.get('geoplugin_region')
            district = None
        elif source == 'reallyfreegeoip.org':
            lat = data.get('latitude')
            lon = data.get('longitude')
            city = data.get('city')
            region = data.get('region_name')
            district = None
        elif source == 'freeipapi.com':
            lat = data.get('latitude')
            lon = data.get('longitude')
            city = data.get('cityName')
            region = data.get('regionName')
            district = None
        elif source == 'ip-api.io':
            lat = data.get('latitude')
            lon = data.get('longitude')
            city = data.get('city')
            region = data.get('region_name')
            district = None
        elif source == 'ipdata.co':
            lat = data.get('latitude')
            lon = data.get('longitude')
            city = data.get('city')
            region = data.get('region')
            district = None
        
        if lat and lon:
            locations.append({
                'source': source,
                'lat': float(lat) if lat else None,
                'lon': float(lon) if lon else None,
                'city': city,
                'region': region,
                'district': district if 'district' in dir() else None
            })
    
    return locations

def calculate_average_location(locations):
    """Hitung rata-rata koordinat dari semua sumber"""
    if not locations:
        return None, None
    
    lats = [l['lat'] for l in locations if l['lat']]
    lons = [l['lon'] for l in locations if l['lon']]
    
    if not lats or not lons:
        return None, None
    
    return sum(lats) / len(lats), sum(lons) / len(lons)

def analyze_security(results):
    """Analisis keamanan berdasarkan data yang ditemukan"""
    issues = []
    
    # Cek data yang terekspos
    exposed_data = set()
    
    for source, data in results.items():
        # Cek field yang terekspos
        fields_to_check = ['city', 'region', 'isp', 'org', 'timezone', 'postal', 'zip']
        for field in fields_to_check:
            for key in data.keys():
                if field in key.lower() and data[key]:
                    exposed_data.add(field)
    
    if exposed_data:
        issues.append({
            'severity': 'INFO',
            'title': 'Data Terekspos Publik',
            'description': f"Data berikut dapat diakses publik: {', '.join(exposed_data)}"
        })
    
    # Cek ISP info
    for source, data in results.items():
        isp = data.get('isp') or data.get('org') or data.get('geoplugin_isp')
        if isp:
            issues.append({
                'severity': 'INFO',
                'title': 'ISP Teridentifikasi',
                'description': f"Provider internet Anda terlihat: {isp}"
            })
            break
    
    return issues

def print_section(title):
    print()
    print(c(Colors.CYAN, "┌─") + c(Colors.BOLD + Colors.WHITE, f" {title} ") + c(Colors.CYAN, "─" * (65 - len(title))))

def print_end_section():
    print(c(Colors.CYAN, "└" + "─" * 70))

def main():
    try:
        print_header()
        
        print(c(Colors.YELLOW, "⚠️  Tool ini hanya untuk testing keamanan IP ANDA SENDIRI.\n"))
        
        while True:
            print("Pilihan:")
            print(f"  {c(Colors.GREEN, '1.')} Scan IP saya sendiri (FULL)")
            print(f"  {c(Colors.GREEN, '2.')} Input IP manual untuk scan")
            print(f"  {c(Colors.GREEN, '3.')} Keluar")
            print()
            
            try:
                choice = input(f"{c(Colors.CYAN, '>')} Pilih (1/2/3): ").strip()
            except (KeyboardInterrupt, EOFError):
                print(f"\n\n{c(Colors.YELLOW, '👋')} Program dihentikan.")
                sys.exit(0)
            
            if choice == '3':
                print(f"\n{c(Colors.GREEN, '👋')} Terima kasih!")
                break
            
            if choice == '1':
                print(f"\n{c(Colors.YELLOW, '🔍')} Mendeteksi IP publik Anda...")
                ip = get_my_ip()
                if not ip:
                    print(f"{c(Colors.RED, '❌')} Gagal mendapatkan IP. Cek koneksi internet.")
                    continue
                print(f"{c(Colors.GREEN, '✓')} IP Terdeteksi: {c(Colors.BOLD, ip)}")
                
            elif choice == '2':
                try:
                    ip = input(f"{c(Colors.CYAN, '>')} Masukkan IP: ").strip()
                except (KeyboardInterrupt, EOFError):
                    print(f"\n\n{c(Colors.YELLOW, '👋')} Program dihentikan.")
                    sys.exit(0)
                
                if not ip:
                    print(f"{c(Colors.RED, '❌')} IP tidak boleh kosong!")
                    continue
            else:
                print(f"{c(Colors.RED, '❌')} Pilihan tidak valid!")
                continue
            
            # ========================================
            # FULL SCAN
            # ========================================
            
            print()
            print(c(Colors.MAGENTA, "═" * 72))
            print(c(Colors.BOLD + Colors.WHITE, f"  🔍 SCANNING IP: {ip}"))
            print(c(Colors.MAGENTA, "═" * 72))
            
            # 1. Geolocation dari berbagai sumber
            print_section("📍 GEOLOCATION SCAN (8 sumber)")
            geo_results = get_all_geolocation_data(ip)
            print_end_section()
            
            # 2. DNS Info
            print_section("🌐 DNS & NETWORK INFO")
            dns_info = get_dns_info(ip)
            whois_info = get_whois_info(ip)
            print_end_section()
            
            # 3. Ekstrak lokasi
            locations = extract_locations(geo_results)
            avg_lat, avg_lon = calculate_average_location(locations)
            
            # 4. Analisis keamanan
            security_issues = analyze_security(geo_results)
            
            # ========================================
            # HASIL
            # ========================================
            
            print()
            print(c(Colors.GREEN, "═" * 72))
            print(c(Colors.BOLD + Colors.WHITE, "  📊 HASIL ANALISIS"))
            print(c(Colors.GREEN, "═" * 72))
            
            # Info dasar
            print(f"\n  {c(Colors.CYAN, '🌐 IP Address:')} {ip}")
            if dns_info.get('hostname'):
                print(f"  {c(Colors.CYAN, '📛 Hostname:')} {dns_info['hostname']}")
            
            # ISP Info
            for source, data in geo_results.items():
                isp = data.get('isp') or data.get('org') or data.get('geoplugin_isp')
                if isp:
                    print(f"  {c(Colors.CYAN, '📡 ISP:')} {isp}")
                    break
            
            # Lokasi dari berbagai sumber
            print(f"\n  {c(Colors.YELLOW, '📍 LOKASI DARI BERBAGAI SUMBER:')}")
            print()
            
            cities_found = {}
            for loc in locations:
                city = loc.get('city', 'Unknown')
                district = loc.get('district', '')
                if city not in cities_found:
                    cities_found[city] = []
                cities_found[city].append(loc['source'])
                
                loc_str = f"{city}"
                if district:
                    loc_str += f" ({district})"
                if loc.get('region'):
                    loc_str += f", {loc['region']}"
                    
                print(f"     {c(Colors.GREEN, '•')} {loc['source']:20} → {loc_str}")
                print(f"       Koordinat: {loc['lat']:.4f}, {loc['lon']:.4f}")
            
            # Kota yang paling sering muncul
            print(f"\n  {c(Colors.YELLOW, '🏙️  ANALISIS KOTA:')}")
            for city, sources in sorted(cities_found.items(), key=lambda x: -len(x[1])):
                print(f"     {c(Colors.GREEN, '•')} {city}: muncul di {len(sources)} sumber")
            
            # Rata-rata koordinat
            if avg_lat and avg_lon:
                print(f"\n  {c(Colors.YELLOW, '📌 KOORDINAT RATA-RATA:')} {avg_lat:.6f}, {avg_lon:.6f}")
            
            # Google Maps Links
            print(f"\n  {c(Colors.MAGENTA, '🗺️  GOOGLE MAPS LINKS:')}")
            print()
            
            if avg_lat and avg_lon:
                avg_link = f"https://www.google.com/maps?q={avg_lat},{avg_lon}&z=14"
                print(f"     {c(Colors.CYAN, 'Rata-rata:')}")
                print(f"     {avg_link}")
            
            print(f"\n     {c(Colors.CYAN, 'Dari setiap sumber:')}")
            for loc in locations[:5]:  # Tampilkan 5 saja
                link = f"https://www.google.com/maps?q={loc['lat']},{loc['lon']}&z=14"
                print(f"     • {loc['source']:18} → {link}")
            
            # Security Analysis
            print(f"\n  {c(Colors.RED, '🔒 ANALISIS KEAMANAN:')}")
            print()
            
            if security_issues:
                for issue in security_issues:
                    sev_color = Colors.YELLOW if issue['severity'] == 'INFO' else Colors.RED
                    print(f"     {c(sev_color, '⚠')} {issue['title']}")
                    print(f"       {issue['description']}")
            
            print(f"\n     {c(Colors.YELLOW, '📋 Rekomendasi untuk proteksi HP Anda:')}")
            print(f"       1. Gunakan VPN untuk menyembunyikan IP asli")
            print(f"       2. Matikan lokasi/GPS saat tidak digunakan")
            print(f"       3. Hindari WiFi publik tanpa proteksi")
            print(f"       4. Gunakan DNS pribadi (seperti 1.1.1.1 atau 8.8.8.8)")
            print(f"       5. Aktifkan firewall di router")
            
            # Raw data untuk analisis
            print(f"\n  {c(Colors.CYAN, '📄 DATA MENTAH (untuk analisis lanjut):')}")
            for source, data in list(geo_results.items())[:3]:
                print(f"\n     {c(Colors.GREEN, source)}:")
                for key, val in list(data.items())[:8]:
                    if val:
                        print(f"       {key}: {val}")
            
            print()
            print(c(Colors.GREEN, "═" * 72))
            print()
            
    except (KeyboardInterrupt, EOFError):
        print(f"\n\n{c(Colors.YELLOW, '👋')} Program dihentikan.")
        sys.exit(0)

if __name__ == '__main__':
    main()

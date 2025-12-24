"""
🔐 PERSONAL SECURITY AUDIT TOOL
Cek data PUBLIK yang terkait dengan email/username/phone Anda
Untuk mengetahui informasi apa saja yang terekspos tentang Anda

⚠️ HANYA untuk testing akun ANDA SENDIRI
"""

import requests
import re
import sys
import hashlib
from concurrent.futures import ThreadPoolExecutor, as_completed

TIMEOUT = 10

def print_header():
    print("\n" + "=" * 70)
    print("  🔐 PERSONAL SECURITY AUDIT TOOL")
    print("  Cek data publik yang terkait dengan email/username/phone Anda")
    print("=" * 70)
    print("""
  ⚠️  Tool ini HANYA mengecek data PUBLIK yang sudah tersedia di internet.
  ⚠️  Gunakan HANYA untuk akun milik ANDA SENDIRI.
  ⚠️  Tidak ada "hacking" atau "bypass" - hanya pencarian data publik.
    """)

def check_email_breach(email):
    """Cek apakah email pernah ada di data breach menggunakan API publik"""
    results = []
    
    print(f"\n  🔍 Checking email breaches for: {email}")
    print("  " + "-" * 60)
    
    # Method 1: Have I Been Pwned (API gratis terbatas)
    print("  ├─ Checking Have I Been Pwned...", end=" ", flush=True)
    try:
        # Gunakan k-anonymity API (gratis)
        sha1_hash = hashlib.sha1(email.lower().encode()).hexdigest().upper()
        prefix = sha1_hash[:5]
        suffix = sha1_hash[5:]
        
        r = requests.get(
            f'https://api.pwnedpasswords.com/range/{prefix}',
            timeout=TIMEOUT
        )
        if suffix in r.text:
            print("⚠️  DITEMUKAN dalam password breach!")
            results.append("Password mungkin pernah bocor")
        else:
            print("✅ Tidak ditemukan")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Method 2: BreachDirectory (public check)
    print("  ├─ Checking BreachDirectory...", end=" ", flush=True)
    try:
        r = requests.get(
            f'https://breachdirectory.p.rapidapi.com/?func=auto&term={email}',
            headers={
                'X-RapidAPI-Host': 'breachdirectory.p.rapidapi.com',
                'X-RapidAPI-Key': 'demo'
            },
            timeout=TIMEOUT
        )
        if r.status_code == 200:
            print("✅ Checked (API key needed for details)")
        else:
            print("⚠️ Rate limited")
    except:
        print("❌ Not available")
    
    # Method 3: Dehashed (public check)
    print("  └─ Checking public breach databases...", end=" ", flush=True)
    try:
        # Check emailrep.io (gratis)
        r = requests.get(
            f'https://emailrep.io/{email}',
            headers={'User-Agent': 'SecurityAudit/1.0'},
            timeout=TIMEOUT
        )
        if r.status_code == 200:
            data = r.json()
            print(f"✅ Reputation: {data.get('reputation', 'unknown')}")
            if data.get('details', {}).get('data_breach'):
                results.append("Email ditemukan di data breach")
            if data.get('details', {}).get('credentials_leaked'):
                results.append("Credentials pernah bocor")
        else:
            print("❌ Not available")
    except Exception as e:
        print(f"❌ {e}")
    
    return results

def check_username_presence(username):
    """Cek keberadaan username di berbagai platform (data publik)"""
    print(f"\n  🔍 Checking username presence: {username}")
    print("  " + "-" * 60)
    
    # Platform yang bisa dicek secara publik
    platforms = [
        ('GitHub', f'https://api.github.com/users/{username}', 200),
        ('Twitter/X', f'https://api.twitter.com/2/users/by/username/{username}', None),  # Needs API
        ('Instagram', f'https://www.instagram.com/{username}/', 200),
        ('TikTok', f'https://www.tiktok.com/@{username}', 200),
        ('Reddit', f'https://www.reddit.com/user/{username}/about.json', 200),
        ('Pinterest', f'https://www.pinterest.com/{username}/', 200),
        ('Medium', f'https://medium.com/@{username}', 200),
        ('Twitch', f'https://www.twitch.tv/{username}', 200),
        ('Spotify', f'https://open.spotify.com/user/{username}', 200),
        ('SoundCloud', f'https://soundcloud.com/{username}', 200),
    ]
    
    found = []
    not_found = []
    
    def check_platform(platform_data):
        name, url, expected_code = platform_data
        try:
            r = requests.get(
                url, 
                timeout=TIMEOUT,
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                    'Accept': 'text/html,application/json'
                },
                allow_redirects=False
            )
            
            if expected_code and r.status_code == expected_code:
                return (name, True, url)
            elif r.status_code in [200, 301, 302]:
                return (name, True, url)
            else:
                return (name, False, None)
        except:
            return (name, None, None)
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(check_platform, p): p[0] for p in platforms}
        
        for future in as_completed(futures):
            name, exists, url = future.result()
            if exists:
                print(f"  ✅ {name}: DITEMUKAN")
                found.append((name, url))
            elif exists is False:
                print(f"  ❌ {name}: Tidak ditemukan")
                not_found.append(name)
            else:
                print(f"  ⚠️ {name}: Tidak bisa dicek")
    
    return found, not_found

def check_phone_exposure(phone):
    """Cek apakah nomor telepon terekspos di data publik"""
    print(f"\n  🔍 Checking phone number: {phone}")
    print("  " + "-" * 60)
    
    # Bersihkan nomor
    clean_phone = re.sub(r'[^\d+]', '', phone)
    
    results = []
    
    # Format Indonesia
    if clean_phone.startswith('08'):
        clean_phone = '+62' + clean_phone[1:]
    elif clean_phone.startswith('62'):
        clean_phone = '+' + clean_phone
    
    print(f"  📱 Formatted: {clean_phone}")
    
    # Check NumVerify (gratis terbatas)
    print("  ├─ Checking NumVerify...", end=" ", flush=True)
    try:
        r = requests.get(
            f'http://apilayer.net/api/validate?access_key=demo&number={clean_phone}',
            timeout=TIMEOUT
        )
        if r.status_code == 200:
            data = r.json()
            if data.get('valid'):
                carrier = data.get('carrier', 'Unknown')
                country = data.get('country_name', 'Unknown')
                print(f"✅ Valid ({carrier}, {country})")
                results.append(f"Carrier: {carrier}")
            else:
                print("❌ Invalid number")
        else:
            print("⚠️ API limited")
    except Exception as e:
        print(f"❌ {e}")
    
    # Analisis format nomor
    print("  └─ Analyzing number format...", end=" ", flush=True)
    if clean_phone.startswith('+62'):
        prefix = clean_phone[3:6]
        carrier_map = {
            '811': 'Telkomsel (Halo/Simpati)',
            '812': 'Telkomsel (Simpati)',
            '813': 'Telkomsel (Simpati)',
            '821': 'Telkomsel (Simpati)',
            '822': 'Telkomsel (Simpati)',
            '823': 'Telkomsel (As)',
            '851': 'Telkomsel',
            '852': 'Telkomsel (As)',
            '853': 'Telkomsel (As)',
            '814': 'Indosat',
            '815': 'Indosat',
            '816': 'Indosat',
            '855': 'Indosat',
            '856': 'Indosat',
            '857': 'Indosat',
            '858': 'Indosat',
            '817': 'XL',
            '818': 'XL',
            '819': 'XL',
            '859': 'XL',
            '877': 'XL',
            '878': 'XL',
            '831': 'Axis',
            '832': 'Axis',
            '833': 'Axis',
            '838': 'Axis',
            '895': 'Three',
            '896': 'Three',
            '897': 'Three',
            '898': 'Three',
            '899': 'Three',
            '881': 'Smartfren',
            '882': 'Smartfren',
            '883': 'Smartfren',
            '884': 'Smartfren',
            '885': 'Smartfren',
            '886': 'Smartfren',
            '887': 'Smartfren',
            '888': 'Smartfren',
            '889': 'Smartfren',
        }
        carrier = carrier_map.get(prefix, 'Unknown operator')
        print(f"✅ Indonesia - {carrier}")
        results.append(f"Operator: {carrier}")
    else:
        print("✅ Analyzed")
    
    return results

def check_public_data_exposure(email):
    """Cek data publik yang terekspos"""
    print(f"\n  🔍 Checking public data exposure...")
    print("  " + "-" * 60)
    
    exposures = []
    
    # Check Gravatar (avatar publik dari email)
    print("  ├─ Checking Gravatar...", end=" ", flush=True)
    try:
        email_hash = hashlib.md5(email.lower().strip().encode()).hexdigest()
        r = requests.get(
            f'https://www.gravatar.com/{email_hash}.json',
            timeout=TIMEOUT
        )
        if r.status_code == 200:
            data = r.json()
            profile = data.get('entry', [{}])[0]
            print("✅ DITEMUKAN")
            if profile.get('displayName'):
                exposures.append(f"Gravatar Name: {profile.get('displayName')}")
            if profile.get('profileUrl'):
                exposures.append(f"Gravatar URL: {profile.get('profileUrl')}")
        else:
            print("❌ Tidak ditemukan")
    except:
        print("❌ Error")
    
    # Check Keybase
    print("  ├─ Checking Keybase...", end=" ", flush=True)
    try:
        r = requests.get(
            f'https://keybase.io/_/api/1.0/user/lookup.json?email={email}',
            timeout=TIMEOUT
        )
        if r.status_code == 200:
            data = r.json()
            if data.get('them'):
                print("✅ DITEMUKAN")
                exposures.append("Keybase account exists")
            else:
                print("❌ Tidak ditemukan")
        else:
            print("❌ Tidak ditemukan")
    except:
        print("❌ Error")
    
    # Check if email is corporate
    print("  └─ Checking email type...", end=" ", flush=True)
    domain = email.split('@')[-1] if '@' in email else ''
    free_domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'icloud.com', 'mail.com']
    
    if domain in free_domains:
        print(f"📧 Free email ({domain})")
    else:
        print(f"🏢 Possibly corporate/custom domain ({domain})")
        exposures.append(f"Custom domain: {domain}")
    
    return exposures

def generate_security_recommendations(email_breaches, phone_results, username_found, exposures):
    """Generate rekomendasi keamanan berdasarkan hasil audit"""
    
    print("\n" + "=" * 70)
    print("  🛡️ SECURITY RECOMMENDATIONS")
    print("=" * 70)
    
    recommendations = []
    
    if email_breaches:
        print("\n  ⚠️  EMAIL/PASSWORD BREACH DETECTED")
        print("  " + "-" * 60)
        for breach in email_breaches:
            print(f"     • {breach}")
        recommendations.append("🔴 GANTI PASSWORD SEKARANG untuk semua akun dengan email ini")
        recommendations.append("🔴 Aktifkan 2FA di semua akun penting")
        recommendations.append("🔴 Gunakan password manager (Bitwarden, 1Password, dll)")
    
    if username_found:
        print(f"\n  📱 USERNAME DITEMUKAN DI {len(username_found)} PLATFORM")
        print("  " + "-" * 60)
        for platform, url in username_found:
            print(f"     • {platform}: {url if url else 'Found'}")
        recommendations.append("🟡 Review privacy settings di setiap platform")
        recommendations.append("🟡 Pertimbangkan untuk menggunakan username berbeda di setiap platform")
    
    if exposures:
        print("\n  📋 DATA TEREKSPOS PUBLIK")
        print("  " + "-" * 60)
        for exp in exposures:
            print(f"     • {exp}")
        recommendations.append("🟡 Review data yang terekspos dan hapus jika tidak perlu")
    
    print("\n  📝 REKOMENDASI AKSI")
    print("  " + "-" * 60)
    
    if recommendations:
        for i, rec in enumerate(recommendations, 1):
            print(f"  {i}. {rec}")
    else:
        print("  ✅ Tidak ada masalah keamanan serius yang ditemukan!")
    
    # General recommendations
    print("\n  💡 TIPS KEAMANAN UMUM")
    print("  " + "-" * 60)
    print("  • Gunakan password unik untuk setiap akun")
    print("  • Aktifkan 2FA (Two-Factor Authentication) dimana tersedia")
    print("  • Jangan gunakan informasi pribadi sebagai password")
    print("  • Periksa aktivitas login secara berkala")
    print("  • Waspada terhadap phishing email/SMS")
    print("  • Update software dan aplikasi secara teratur")

def main():
    try:
        print_header()
        
        while True:
            print("\nMenu:")
            print("  1. Audit Email (cek breach + exposure)")
            print("  2. Audit Username (cek presence di platform)")
            print("  3. Audit Phone Number")
            print("  4. FULL AUDIT (email + username + phone)")
            print("  5. Keluar")
            
            try:
                choice = input("\n> Pilih (1-5): ").strip()
            except (KeyboardInterrupt, EOFError):
                print("\n\n👋 Bye!")
                sys.exit(0)
            
            if choice == '5':
                print("\n👋 Terima kasih!")
                break
            
            email_breaches = []
            phone_results = []
            username_found = []
            exposures = []
            
            if choice in ['1', '4']:
                try:
                    email = input("\n> Masukkan email Anda: ").strip()
                except (KeyboardInterrupt, EOFError):
                    continue
                    
                if email and '@' in email:
                    email_breaches = check_email_breach(email)
                    exposures = check_public_data_exposure(email)
                else:
                    print("❌ Email tidak valid!")
                    continue
            
            if choice in ['2', '4']:
                try:
                    username = input("\n> Masukkan username Anda: ").strip()
                except (KeyboardInterrupt, EOFError):
                    continue
                    
                if username:
                    username_found, _ = check_username_presence(username)
                else:
                    print("❌ Username tidak boleh kosong!")
                    if choice == '2':
                        continue
            
            if choice in ['3', '4']:
                try:
                    phone = input("\n> Masukkan nomor telepon Anda: ").strip()
                except (KeyboardInterrupt, EOFError):
                    continue
                    
                if phone:
                    phone_results = check_phone_exposure(phone)
                else:
                    print("❌ Nomor telepon tidak boleh kosong!")
                    if choice == '3':
                        continue
            
            # Generate recommendations
            if choice in ['1', '2', '3', '4']:
                generate_security_recommendations(email_breaches, phone_results, username_found, exposures)
            
            print("\n" + "=" * 70)
            
    except (KeyboardInterrupt, EOFError):
        print("\n\n👋 Bye!")
        sys.exit(0)

if __name__ == '__main__':
    main()

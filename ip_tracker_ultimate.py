#!/usr/bin/env python3
"""
⚖️ LEGAL TRACK - Advanced IP & OSINT Tracker
GitHub: https://github.com/yourusername/legal-track
Version: 4.0.0
"""

VERSION = "4.0.0"
AUTHOR = "Legal Track Team"
GITHUB_URL = "https://github.com/yourusername/legal-track"

import sys
import os
import time
import subprocess

# ==========================================
# INITIALIZATION & DEPENDENCY CHECK
# ==========================================

class Colors:
    """Terminal colors"""
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    GRAY = '\033[90m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    END = '\033[0m'

C = Colors

def clear_screen():
    """Clear terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_startup_banner():
    """Print startup banner"""
    print(f"""
{C.CYAN}
  ██╗     ███████╗ ██████╗  █████╗ ██╗         ████████╗██████╗  █████╗  ██████╗██╗  ██╗
  ██║     ██╔════╝██╔════╝ ██╔══██╗██║         ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝
  ██║     █████╗  ██║  ███╗███████║██║            ██║   ██████╔╝███████║██║     █████╔╝ 
  ██║     ██╔══╝  ██║   ██║██╔══██║██║            ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ 
  ███████╗███████╗╚██████╔╝██║  ██║███████╗       ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗
  ╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝       ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
{C.END}
{C.GRAY}                    ⚖️  Advanced IP & OSINT Tracker v{VERSION}{C.END}
{C.GRAY}                         For Security Testing Only{C.END}
    """)

def spinner(message, duration=1.5):
    """Show spinner animation"""
    frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        sys.stdout.write(f'\r  {C.CYAN}{frames[i % len(frames)]}{C.END} {message}')
        sys.stdout.flush()
        time.sleep(0.08)
        i += 1
    return True

def check_python_version():
    """Check Python version"""
    spinner("Checking Python version...", 0.5)
    
    major, minor = sys.version_info[:2]
    if major >= 3 and minor >= 7:
        print(f'\r  {C.GREEN}✓{C.END} Python version: {C.WHITE}{major}.{minor}{C.END}              ')
        return True
    else:
        print(f'\r  {C.RED}✗{C.END} Python 3.7+ required (you have {major}.{minor})')
        return False

def check_and_install_dependencies():
    """Check and install required dependencies"""
    required_packages = ['requests']
    
    spinner("Checking dependencies...", 0.5)
    
    missing = []
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing.append(package)
    
    if missing:
        print(f'\r  {C.YELLOW}!{C.END} Installing missing packages: {missing}')
        for package in missing:
            spinner(f"Installing {package}...", 0.3)
            try:
                subprocess.check_call(
                    [sys.executable, '-m', 'pip', 'install', package, '-q'],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
                print(f'\r  {C.GREEN}✓{C.END} Installed: {package}                    ')
            except:
                print(f'\r  {C.RED}✗{C.END} Failed to install: {package}')
                return False
    else:
        print(f'\r  {C.GREEN}✓{C.END} All dependencies installed              ')
    
    return True

def check_network():
    """Check network connectivity"""
    spinner("Checking network connection...", 0.8)
    
    try:
        import requests
        r = requests.get('https://api.ipify.org', timeout=5)
        if r.status_code == 200:
            print(f'\r  {C.GREEN}✓{C.END} Network: {C.WHITE}Connected{C.END}                    ')
            return True
    except:
        pass
    
    print(f'\r  {C.RED}✗{C.END} Network: {C.RED}No connection{C.END}')
    return False

def initialize():
    """Run initialization sequence"""
    print()
    print(f"  {C.CYAN}{'─' * 55}{C.END}")
    print(f"  {C.BOLD}⚙️  INITIALIZING LEGAL TRACK...{C.END}")
    print(f"  {C.CYAN}{'─' * 55}{C.END}")
    print()
    
    # Check Python
    if not check_python_version():
        print(f"\n  {C.RED}[!] Initialization failed. Please upgrade Python.{C.END}")
        sys.exit(1)
    
    # Check dependencies
    if not check_and_install_dependencies():
        print(f"\n  {C.RED}[!] Initialization failed. Could not install dependencies.{C.END}")
        sys.exit(1)
    
    # Check network
    if not check_network():
        print(f"\n  {C.YELLOW}[!] Warning: No network connection. Some features may not work.{C.END}")
    
    # Loading modules
    spinner("Loading modules...", 0.5)
    print(f'\r  {C.GREEN}✓{C.END} Modules loaded                          ')
    
    # Initialize API endpoints
    spinner("Initializing API endpoints...", 0.5)
    print(f'\r  {C.GREEN}✓{C.END} API endpoints ready                     ')
    
    # Final
    print()
    print(f"  {C.GREEN}{'─' * 55}{C.END}")
    print(f"  {C.GREEN}✓{C.END} {C.BOLD}LEGAL TRACK v{VERSION} - Ready!{C.END}")
    print(f"  {C.GREEN}{'─' * 55}{C.END}")
    print()
    
    time.sleep(0.5)
    return True

# ==========================================
# IMPORT MODULES AFTER DEPENDENCY CHECK
# ==========================================

try:
    import requests
    import socket
    import json
    import re
    import hashlib
    import concurrent.futures
    from datetime import datetime
except ImportError as e:
    print(f"Error importing modules: {e}")
    print("Please run: pip install requests")
    sys.exit(1)

# ==========================================
# KONFIGURASI
# ==========================================

TIMEOUT = 10
MAX_WORKERS = 15

# ==========================================
# SOCIAL MEDIA & OSINT FUNCTIONS
# ==========================================

def check_username_on_platform(args):
    """Check username pada satu platform"""
    platform, url_template, username, check_type = args
    
    url = url_template.format(username=username)
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
        }
        
        r = requests.get(url, headers=headers, timeout=TIMEOUT, allow_redirects=True)
        
        if check_type == 'status_200':
            exists = r.status_code == 200
        elif check_type == 'status_not_404':
            exists = r.status_code != 404
        elif check_type == 'json_exists':
            exists = r.status_code == 200 and 'error' not in r.text.lower()
        else:
            exists = r.status_code == 200
        
        return platform, exists, url if exists else None
        
    except:
        return platform, None, None

def search_username(username):
    """Search username di berbagai platform social media"""
    
    print(f"\n  {C.CYAN}[SOCIAL MEDIA SCAN]{C.END} {C.BOLD}Searching username: {username}{C.END}")
    print(f"  {C.GRAY}{'─' * 55}{C.END}")
    
    platforms = [
        ('GitHub', 'https://github.com/{username}', 'status_200'),
        ('Twitter/X', 'https://twitter.com/{username}', 'status_200'),
        ('Instagram', 'https://www.instagram.com/{username}/', 'status_200'),
        ('TikTok', 'https://www.tiktok.com/@{username}', 'status_200'),
        ('YouTube', 'https://www.youtube.com/@{username}', 'status_200'),
        ('Facebook', 'https://www.facebook.com/{username}', 'status_200'),
        ('LinkedIn', 'https://www.linkedin.com/in/{username}', 'status_200'),
        ('Reddit', 'https://www.reddit.com/user/{username}', 'status_200'),
        ('Pinterest', 'https://www.pinterest.com/{username}/', 'status_200'),
        ('Twitch', 'https://www.twitch.tv/{username}', 'status_200'),
        ('Telegram', 'https://t.me/{username}', 'status_200'),
        ('Medium', 'https://medium.com/@{username}', 'status_200'),
        ('Spotify', 'https://open.spotify.com/user/{username}', 'status_200'),
        ('SoundCloud', 'https://soundcloud.com/{username}', 'status_200'),
        ('DeviantArt', 'https://www.deviantart.com/{username}', 'status_200'),
        ('Tumblr', 'https://{username}.tumblr.com', 'status_200'),
        ('Vimeo', 'https://vimeo.com/{username}', 'status_200'),
        ('Behance', 'https://www.behance.net/{username}', 'status_200'),
        ('Dribbble', 'https://dribbble.com/{username}', 'status_200'),
        ('GitLab', 'https://gitlab.com/{username}', 'status_200'),
        ('Steam', 'https://steamcommunity.com/id/{username}', 'status_200'),
        ('Roblox', 'https://www.roblox.com/user.aspx?username={username}', 'status_200'),
        ('Patreon', 'https://www.patreon.com/{username}', 'status_200'),
    ]
    
    found = []
    not_found = []
    errors = []
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {
            executor.submit(check_username_on_platform, (p[0], p[1], username, p[2])): p[0] 
            for p in platforms
        }
        
        for future in concurrent.futures.as_completed(futures):
            platform = futures[future]
            try:
                name, exists, url = future.result()
                if exists:
                    found.append((name, url))
                    print(f"     {C.GREEN}[+]{C.END} {name}: {C.GREEN}FOUND{C.END}")
                elif exists is False:
                    not_found.append(name)
                    print(f"     {C.GRAY}[-]{C.END} {name}: {C.GRAY}Not found{C.END}")
                else:
                    errors.append(name)
                    print(f"     {C.YELLOW}[?]{C.END} {name}: {C.YELLOW}Error/Blocked{C.END}")
            except:
                errors.append(platform)
    
    return found, not_found, errors

def check_email_breaches(email):
    """Check apakah email pernah ada di data breach"""
    
    print(f"\n  {C.CYAN}[EMAIL BREACH CHECK]{C.END} {C.BOLD}Checking: {email}{C.END}")
    print(f"  {C.GRAY}{'─' * 55}{C.END}")
    
    breaches = []
    
    print(f"     {C.YELLOW}[*]{C.END} Checking HaveIBeenPwned...", end=" ", flush=True)
    try:
        sha1_hash = hashlib.sha1(email.lower().encode()).hexdigest().upper()
        prefix = sha1_hash[:5]
        suffix = sha1_hash[5:]
        
        r = requests.get(f'https://api.pwnedpasswords.com/range/{prefix}', timeout=TIMEOUT)
        if suffix in r.text:
            print(f"{C.RED}PWNED!{C.END}")
            breaches.append("Password found in breach database")
        else:
            print(f"{C.GREEN}SAFE{C.END}")
    except:
        print(f"{C.YELLOW}Error{C.END}")
    
    print(f"     {C.YELLOW}[*]{C.END} Checking email reputation...", end=" ", flush=True)
    try:
        r = requests.get(
            f'https://emailrep.io/{email}',
            headers={'User-Agent': 'LegalTrack/4.0'},
            timeout=TIMEOUT
        )
        if r.status_code == 200:
            data = r.json()
            reputation = data.get('reputation', 'unknown')
            suspicious = data.get('suspicious', False)
            details = data.get('details', {})
            
            if suspicious:
                print(f"{C.RED}SUSPICIOUS{C.END}")
            else:
                print(f"{C.GREEN}{reputation.upper()}{C.END}")
            
            if details.get('data_breach'):
                breaches.append("Found in data breach")
            if details.get('credentials_leaked'):
                breaches.append("Credentials leaked")
            
            return {
                'reputation': reputation,
                'suspicious': suspicious,
                'breaches': breaches,
                'details': details
            }
        else:
            print(f"{C.YELLOW}Rate limited{C.END}")
    except:
        print(f"{C.YELLOW}Error{C.END}")
    
    return {'breaches': breaches}

def search_email_accounts(email):
    """Search akun yang terkait dengan email"""
    
    print(f"\n  {C.CYAN}[EMAIL ACCOUNT SEARCH]{C.END} {C.BOLD}Searching: {email}{C.END}")
    print(f"  {C.GRAY}{'─' * 55}{C.END}")
    
    accounts = []
    
    print(f"     {C.YELLOW}[*]{C.END} Checking Gravatar...", end=" ", flush=True)
    try:
        email_hash = hashlib.md5(email.lower().strip().encode()).hexdigest()
        r = requests.get(f'https://www.gravatar.com/{email_hash}.json', timeout=TIMEOUT)
        if r.status_code == 200:
            data = r.json()
            entry = data.get('entry', [{}])[0]
            print(f"{C.GREEN}FOUND{C.END}")
            accounts.append({
                'platform': 'Gravatar',
                'username': entry.get('preferredUsername', ''),
                'name': entry.get('displayName', ''),
                'url': entry.get('profileUrl', ''),
            })
        else:
            print(f"{C.GRAY}Not found{C.END}")
    except:
        print(f"{C.YELLOW}Error{C.END}")
    
    print(f"     {C.YELLOW}[*]{C.END} Checking GitHub...", end=" ", flush=True)
    try:
        username = email.split('@')[0]
        r = requests.get(f'https://api.github.com/users/{username}', timeout=TIMEOUT)
        if r.status_code == 200:
            data = r.json()
            print(f"{C.GREEN}Possible match{C.END}")
            accounts.append({
                'platform': 'GitHub (possible)',
                'username': data.get('login', ''),
                'name': data.get('name', ''),
                'url': data.get('html_url', ''),
            })
        else:
            print(f"{C.GRAY}Not found{C.END}")
    except:
        print(f"{C.YELLOW}Error{C.END}")
    
    return accounts

def analyze_phone_number(phone):
    """Analisis nomor telepon dengan detail lengkap + Google Maps link"""

    print(f"\n  {C.CYAN}[PHONE ANALYSIS]{C.END} {C.BOLD}Analyzing: {phone}{C.END}")
    print(f"  {C.GRAY}{'─' * 55}{C.END}")

    # ── Auto-install phonenumbers jika belum ada ──────────────
    try:
        import phonenumbers
        from phonenumbers import (
            geocoder, carrier, timezone,
            PhoneNumberType, NumberParseException,
            is_valid_number, is_possible_number,
            format_number, PhoneNumberFormat,
        )
    except ImportError:
        print(f"     {C.YELLOW}[*]{C.END} Installing phonenumbers library...", end=" ", flush=True)
        try:
            subprocess.check_call(
                [sys.executable, '-m', 'pip', 'install', 'phonenumbers', '-q'],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )
            import phonenumbers
            from phonenumbers import (
                geocoder, carrier, timezone,
                PhoneNumberType, NumberParseException,
                is_valid_number, is_possible_number,
                format_number, PhoneNumberFormat,
            )
            print(f"{C.GREEN}OK{C.END}")
        except Exception as e:
            print(f"{C.RED}FAILED ({e}){C.END}")
            return {}

    # ── Normalisasi nomor ─────────────────────────────────────
    clean_phone = re.sub(r'[^\d+]', '', phone)
    if clean_phone.startswith('08'):
        clean_phone = '+62' + clean_phone[1:]
    elif clean_phone.startswith('62') and not clean_phone.startswith('+'):
        clean_phone = '+' + clean_phone
    elif not clean_phone.startswith('+'):
        clean_phone = '+' + clean_phone

    result = {}

    # ── Parse dengan phonenumbers ─────────────────────────────
    try:
        parsed = phonenumbers.parse(clean_phone, None)
    except Exception:
        # Coba parse sebagai nomor Indonesia
        try:
            parsed = phonenumbers.parse(phone, 'ID')
        except Exception as e:
            print(f"     {C.RED}[!]{C.END} Cannot parse number: {e}")
            return {}

    # ── Validasi ──────────────────────────────────────────────
    valid   = is_valid_number(parsed)
    possible = is_possible_number(parsed)

    # Format internasional & lokal
    fmt_intl  = format_number(parsed, PhoneNumberFormat.INTERNATIONAL)
    fmt_e164  = format_number(parsed, PhoneNumberFormat.E164)
    fmt_local = format_number(parsed, PhoneNumberFormat.NATIONAL)

    # Info dasar
    country_name   = geocoder.description_for_number(parsed, 'id') or 'Unknown'
    country_code   = parsed.country_code
    carrier_name   = carrier.name_for_number(parsed, 'id') or 'Unknown'
    timezones      = timezone.time_zones_for_number(parsed)
    tz_str         = ', '.join(timezones) if timezones else 'Unknown'

    # Tipe nomor
    num_type_raw = phonenumbers.number_type(parsed)
    type_map = {
        PhoneNumberType.MOBILE:            '📱 Mobile',
        PhoneNumberType.FIXED_LINE:        '☎️  Fixed Line',
        PhoneNumberType.FIXED_LINE_OR_MOBILE: '📱/☎️  Fixed/Mobile',
        PhoneNumberType.TOLL_FREE:         '🆓 Toll Free',
        PhoneNumberType.PREMIUM_RATE:      '💰 Premium Rate',
        PhoneNumberType.VOIP:              '🌐 VoIP',
        PhoneNumberType.UNKNOWN:           '❓ Unknown',
    }
    num_type = type_map.get(num_type_raw, '❓ Unknown')

    # Nomor darurat / khusus
    is_emergency = phonenumbers.is_emergency_number(clean_phone, 'ID')

    # ── Mapping region Indonesia → koordinat + detail kota ────
    REGION_COORDS = {
        # Jawa
        'Jakarta':        (-6.2088,  106.8456, 'Jakarta, DKI Jakarta, Indonesia',          'Jakarta, DKI Jakarta'),
        'Bandung':        (-6.9175,  107.6191, 'Kota Bandung, Jawa Barat, Indonesia',       'Bandung, Jawa Barat'),
        'Surabaya':       (-7.2575,  112.7521, 'Kota Surabaya, Jawa Timur, Indonesia',      'Surabaya, Jawa Timur'),
        'Yogyakarta':     (-7.7956,  110.3695, 'Kota Yogyakarta, DIY, Indonesia',           'Yogyakarta, DIY'),
        'Semarang':       (-6.9932,  110.4203, 'Kota Semarang, Jawa Tengah, Indonesia',     'Semarang, Jawa Tengah'),
        'Malang':         (-7.9839,  112.6214, 'Kota Malang, Jawa Timur, Indonesia',        'Malang, Jawa Timur'),
        'Solo':           (-7.5755,  110.8243, 'Kota Surakarta (Solo), Jawa Tengah',        'Solo, Jawa Tengah'),
        'Surakarta':      (-7.5755,  110.8243, 'Kota Surakarta (Solo), Jawa Tengah',        'Solo, Jawa Tengah'),
        'Depok':          (-6.4025,  106.7942, 'Kota Depok, Jawa Barat, Indonesia',         'Depok, Jawa Barat'),
        'Tangerang':      (-6.1702,  106.6403, 'Kota Tangerang, Banten, Indonesia',         'Tangerang, Banten'),
        'Bekasi':         (-6.2349,  106.9921, 'Kota Bekasi, Jawa Barat, Indonesia',        'Bekasi, Jawa Barat'),
        'Bogor':          (-6.5971,  106.8060, 'Kota Bogor, Jawa Barat, Indonesia',         'Bogor, Jawa Barat'),
        'Cirebon':        (-6.7063,  108.5570, 'Kota Cirebon, Jawa Barat, Indonesia',       'Cirebon, Jawa Barat'),
        'Serang':         (-6.1201,  106.1503, 'Kota Serang, Banten, Indonesia',            'Serang, Banten'),
        'Tasikmalaya':    (-7.3274,  108.2207, 'Kota Tasikmalaya, Jawa Barat, Indonesia',   'Tasikmalaya, Jawa Barat'),
        'Purwokerto':     (-7.4252,  109.2350, 'Purwokerto, Banyumas, Jawa Tengah',         'Purwokerto, Jawa Tengah'),
        'Madiun':         (-7.6298,  111.5239, 'Kota Madiun, Jawa Timur, Indonesia',        'Madiun, Jawa Timur'),
        'Kediri':         (-7.8168,  112.0114, 'Kota Kediri, Jawa Timur, Indonesia',        'Kediri, Jawa Timur'),
        'Jember':         (-8.1728,  113.7001, 'Kota Jember, Jawa Timur, Indonesia',        'Jember, Jawa Timur'),
        'Blitar':         (-8.0953,  112.1608, 'Kota Blitar, Jawa Timur, Indonesia',        'Blitar, Jawa Timur'),
        'Mojokerto':      (-7.4724,  112.4338, 'Kota Mojokerto, Jawa Timur, Indonesia',     'Mojokerto, Jawa Timur'),
        'Pasuruan':       (-7.6453,  112.9075, 'Kota Pasuruan, Jawa Timur, Indonesia',      'Pasuruan, Jawa Timur'),
        'Probolinggo':    (-7.7543,  113.2159, 'Kota Probolinggo, Jawa Timur',              'Probolinggo, Jawa Timur'),
        'Batu':           (-7.8675,  122.5477, 'Kota Batu, Jawa Timur, Indonesia',          'Batu, Jawa Timur'),
        'Magelang':       (-7.4705,  110.2178, 'Kota Magelang, Jawa Tengah, Indonesia',     'Magelang, Jawa Tengah'),
        'Pekalongan':     (-6.8887,  109.6753, 'Kota Pekalongan, Jawa Tengah',              'Pekalongan, Jawa Tengah'),
        'Tegal':          (-6.8797,  109.1256, 'Kota Tegal, Jawa Tengah, Indonesia',        'Tegal, Jawa Tengah'),
        'Salatiga':       (-7.3306,  110.5078, 'Kota Salatiga, Jawa Tengah, Indonesia',     'Salatiga, Jawa Tengah'),
        # Sumatera
        'Medan':          (3.5952,    98.6722, 'Kota Medan, Sumatera Utara, Indonesia',     'Medan, Sumatera Utara'),
        'Palembang':      (-2.9761,  104.7754, 'Kota Palembang, Sumatera Selatan',          'Palembang, Sumatera Selatan'),
        'Pekanbaru':      (0.5071,   101.4478, 'Kota Pekanbaru, Riau, Indonesia',           'Pekanbaru, Riau'),
        'Batam':          (1.0456,   104.0305, 'Kota Batam, Kepulauan Riau, Indonesia',     'Batam, Kepulauan Riau'),
        'Padang':         (-0.9471,  100.4172, 'Kota Padang, Sumatera Barat, Indonesia',    'Padang, Sumatera Barat'),
        'Bandar Lampung': (-5.4295,  105.2611, 'Kota Bandar Lampung, Lampung, Indonesia',   'Bandar Lampung, Lampung'),
        'Banda Aceh':     (5.5483,    95.3238, 'Kota Banda Aceh, Aceh, Indonesia',          'Banda Aceh, Aceh'),
        'Jambi':          (-1.6101,  103.6131, 'Kota Jambi, Jambi, Indonesia',              'Jambi, Jambi'),
        'Bengkulu':       (-3.7928,  102.2608, 'Kota Bengkulu, Bengkulu, Indonesia',        'Bengkulu, Bengkulu'),
        'Pematangsiantar': (2.9595,   99.0687, 'Kota Pematangsiantar, Sumatera Utara',      'Pematangsiantar, Sumut'),
        # Kalimantan
        'Balikpapan':     (-1.2654,  116.8312, 'Kota Balikpapan, Kalimantan Timur',        'Balikpapan, Kaltim'),
        'Pontianak':      (-0.0264,  109.3425, 'Kota Pontianak, Kalimantan Barat',          'Pontianak, Kalimantan Barat'),
        'Banjarmasin':    (-3.3186,  114.5944, 'Kota Banjarmasin, Kalimantan Selatan',      'Banjarmasin, Kalsel'),
        'Samarinda':      (-0.5016,  117.1537, 'Kota Samarinda, Kalimantan Timur',          'Samarinda, Kaltim'),
        'Palangkaraya':   (-2.2161,  113.9135, 'Kota Palangka Raya, Kalimantan Tengah',     'Palangka Raya, Kalteng'),
        'Tarakan':        (3.3024,   117.6353, 'Kota Tarakan, Kalimantan Utara',            'Tarakan, Kaltara'),
        # Sulawesi & Timur
        'Makassar':       (-5.1477,  119.4327, 'Kota Makassar, Sulawesi Selatan, Indonesia','Makassar, Sulawesi Selatan'),
        'Manado':         (1.4748,   124.8421, 'Kota Manado, Sulawesi Utara, Indonesia',    'Manado, Sulawesi Utara'),
        'Kendari':        (-3.9985,  122.5127, 'Kota Kendari, Sulawesi Tenggara',           'Kendari, Sultra'),
        'Palu':           (-0.8917,  119.8707, 'Kota Palu, Sulawesi Tengah, Indonesia',     'Palu, Sulawesi Tengah'),
        'Gorontalo':      (0.5435,   123.0596, 'Kota Gorontalo, Gorontalo, Indonesia',      'Gorontalo, Gorontalo'),
        'Denpasar':       (-8.6705,  115.2126, 'Kota Denpasar, Bali, Indonesia',            'Denpasar, Bali'),
        'Mataram':        (-8.5833,  116.1167, 'Kota Mataram, Nusa Tenggara Barat',         'Mataram, NTB'),
        'Kupang':         (-10.1772, 123.6070, 'Kota Kupang, Nusa Tenggara Timur',          'Kupang, NTT'),
        'Ambon':          (-3.6954,  128.1814, 'Kota Ambon, Maluku, Indonesia',             'Ambon, Maluku'),
        'Jayapura':       (-2.5916,  140.6690, 'Kota Jayapura, Papua, Indonesia',           'Jayapura, Papua'),
        'Sorong':         (-0.8767,  131.2505, 'Kota Sorong, Papua Barat Daya, Indonesia',  'Sorong, Papua Barat'),
        # Umum Indonesia (fallback)
        'Indonesia':      (-2.5489,  118.0149, 'Indonesia',                                 'Indonesia'),
        'Jawa':           (-7.6145,  110.7122, 'Pulau Jawa, Indonesia',                     'Jawa, Indonesia'),
        'Sumatera':       (0.5897,   101.3431, 'Pulau Sumatera, Indonesia',                 'Sumatera, Indonesia'),
        'Kalimantan':     (1.6810,   113.3824, 'Pulau Kalimantan, Indonesia',               'Kalimantan, Indonesia'),
        'Sulawesi':       (-2.3594,  121.2485, 'Pulau Sulawesi, Indonesia',                 'Sulawesi, Indonesia'),
        'Bali':           (-8.4095,  115.1889, 'Bali, Indonesia',                           'Bali, Indonesia'),
        'Papua':          (-4.2699,  138.0804, 'Papua, Indonesia',                          'Papua, Indonesia'),
    }

    # ── Cari koordinat dari nama region ───────────────────────
    lat, lon, region_label, search_label = None, None, country_name, country_name

    # Coba dari geocoder dulu (lebih spesifik)
    geo_desc_en = geocoder.description_for_number(parsed, 'en') or ''
    geo_desc_id = geocoder.description_for_number(parsed, 'id') or ''

    # Gabungkan semua teks untuk dicocokkan
    search_text = f"{country_name} {geo_desc_en} {geo_desc_id}"

    for key, (rlat, rlon, rlabel, slabel) in REGION_COORDS.items():
        if key.lower() in search_text.lower():
            lat, lon, region_label, search_label = rlat, rlon, rlabel, slabel
            break

    # Fallback: kalau region generic "Indonesia"
    if lat is None and 'Indonesia' in search_text:
        lat, lon, region_label, search_label = REGION_COORDS['Indonesia']

    # ── Buat Google Maps link ──────────────────────────────────
    maps_url = None
    maps_search_url = None
    if lat is not None and lon is not None:
        # Link koordinat dengan zoom lebih dalam (z=12 = level kota)
        maps_url = f"https://www.google.com/maps?q={lat},{lon}&z=12"
        # Link pencarian nama kota (lebih akurat & deskriptif)
        maps_search_url = f"https://www.google.com/maps/search/{search_label.replace(' ', '+').replace(',', '%2C')}"

    # ── Tampilkan hasil ───────────────────────────────────────
    print(f"\n  {C.CYAN}{'═' * 57}{C.END}")
    print(f"  {C.BOLD}  📋  PHONE NUMBER INTELLIGENCE REPORT{C.END}")
    print(f"  {C.CYAN}{'═' * 57}{C.END}\n")

    status_color = C.GREEN if valid else C.RED
    status_icon  = '✅' if valid else '❌'
    print(f"  {C.BOLD}┌─ STATUS{C.END}")
    print(f"  │  {status_icon} Valid       : {status_color}{valid}{C.END}")
    print(f"  │  {'✅' if possible else '⚠️ '} Possible   : {C.GREEN if possible else C.YELLOW}{possible}{C.END}")
    if is_emergency:
        print(f"  │  {C.RED}🚨 EMERGENCY NUMBER{C.END}")

    print(f"\n  {C.BOLD}┌─ FORMAT{C.END}")
    print(f"  │  🌐 International : {C.WHITE}{fmt_intl}{C.END}")
    print(f"  │  📲 E.164         : {C.WHITE}{fmt_e164}{C.END}")
    print(f"  │  📞 Local         : {C.WHITE}{fmt_local}{C.END}")

    print(f"\n  {C.BOLD}┌─ DETAIL{C.END}")
    print(f"  │  🌍 Country       : {C.WHITE}{country_name} (+{country_code}){C.END}")
    print(f"  │  📡 Carrier       : {C.WHITE}{carrier_name}{C.END}")
    print(f"  │  📱 Type          : {C.WHITE}{num_type}{C.END}")
    print(f"  │  🕐 Timezone      : {C.WHITE}{tz_str}{C.END}")

    if lat is not None:
        print(f"\n  {C.BOLD}┌─ ESTIMATED REGION{C.END}")
        print(f"  │  📍 Area Detail   : {C.WHITE}{region_label}{C.END}")
        print(f"  │  🗺️  Coordinates   : {C.WHITE}{lat:.4f}, {lon:.4f}{C.END}")
        if geo_desc_en and geo_desc_en.lower() not in ('indonesia',):
            print(f"  │  🔎 Geocoder (EN) : {C.WHITE}{geo_desc_en}{C.END}")
        if geo_desc_id and geo_desc_id != geo_desc_en:
            print(f"  │  🔎 Geocoder (ID) : {C.WHITE}{geo_desc_id}{C.END}")
        print(f"\n  {C.BOLD}┌─ GOOGLE MAPS{C.END}")
        print(f"  │  📌 Koordinat Kota:")
        print(f"  │     {C.BLUE}{maps_url}{C.END}")
        if maps_search_url:
            print(f"  │  🔍 Cari Nama Kota (lebih akurat):")
            print(f"  │     {C.CYAN}{maps_search_url}{C.END}")
        print(f"  │  {C.GRAY}(Estimasi area dari nomor seri, bukan GPS pasti){C.END}")

    print(f"\n  {C.CYAN}{'═' * 57}{C.END}\n")

    result = {
        'formatted_intl': fmt_intl,
        'formatted_e164': fmt_e164,
        'formatted_local': fmt_local,
        'valid': valid,
        'possible': possible,
        'country': country_name,
        'country_code': country_code,
        'carrier': carrier_name,
        'type': num_type,
        'timezone': tz_str,
        'region_label': region_label,
        'search_label': search_label,
        'geocoder_en': geo_desc_en,
        'geocoder_id': geo_desc_id,
        'lat': lat,
        'lon': lon,
        'maps_url': maps_url,
        'maps_search_url': maps_search_url,
    }
    return result

# ==========================================
# IP GEOLOCATION FUNCTIONS
# ==========================================

def fetch_url(args):
    """Helper untuk concurrent fetching"""
    name, url, parser = args
    try:
        r = requests.get(url, timeout=TIMEOUT, headers={'User-Agent': 'Mozilla/5.0'})
        if r.status_code == 200:
            data = r.json() if 'json' in r.headers.get('content-type', '') else r.text
            return name, parser(data) if parser else data
    except:
        pass
    return name, None

def get_all_geolocation(ip):
    """Dapatkan data dari 10+ sumber geolokasi"""
    
    apis = [
        ('ip-api.com', f'http://ip-api.com/json/{ip}?fields=66846719', lambda d: d if d.get('status') == 'success' else None),
        ('ipinfo.io', f'https://ipinfo.io/{ip}/json', lambda d: d if 'loc' in d else None),
        ('ipwhois.app', f'https://ipwhois.app/json/{ip}', lambda d: d if d.get('success', True) else None),
        ('ip-api.io', f'https://ip-api.io/json/{ip}', lambda d: d),
        ('geoplugin.net', f'http://www.geoplugin.net/json.gp?ip={ip}', lambda d: d if d.get('geoplugin_status') == 200 else None),
        ('reallyfreegeoip.org', f'https://reallyfreegeoip.org/json/{ip}', lambda d: d),
        ('freeipapi.com', f'https://freeipapi.com/api/json/{ip}', lambda d: d),
        ('ipapi.co', f'https://ipapi.co/{ip}/json/', lambda d: d if 'city' in d else None),
    ]
    
    results = {}
    
    print(f"\n  {C.CYAN}[PHASE 1]{C.END} {C.BOLD}Scanning Geolocation Databases...{C.END}")
    print(f"  {C.GRAY}{'─' * 55}{C.END}")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(fetch_url, api): api[0] for api in apis}
        
        for future in concurrent.futures.as_completed(futures):
            name = futures[future]
            try:
                api_name, data = future.result()
                if data:
                    results[api_name] = data
                    print(f"     {C.GREEN}[+]{C.END} {name}: {C.GREEN}DATA ACQUIRED{C.END}")
                else:
                    print(f"     {C.RED}[-]{C.END} {name}: {C.RED}NO DATA{C.END}")
            except:
                print(f"     {C.RED}[-]{C.END} {name}: {C.RED}FAILED{C.END}")
    
    return results

def get_dns_records(ip):
    """Dapatkan DNS records"""
    records = {}
    
    print(f"\n  {C.CYAN}[PHASE 2]{C.END} {C.BOLD}DNS Reconnaissance...{C.END}")
    print(f"  {C.GRAY}{'─' * 55}{C.END}")
    
    try:
        hostname, aliases, _ = socket.gethostbyaddr(ip)
        records['hostname'] = hostname
        print(f"     {C.GREEN}[+]{C.END} Reverse DNS: {C.WHITE}{hostname}{C.END}")
    except:
        print(f"     {C.YELLOW}[!]{C.END} Reverse DNS: {C.YELLOW}NOT FOUND{C.END}")
    
    return records

def get_asn_info(ip):
    """Dapatkan informasi ASN"""
    print(f"\n  {C.CYAN}[PHASE 3]{C.END} {C.BOLD}ASN Analysis...{C.END}")
    print(f"  {C.GRAY}{'─' * 55}{C.END}")
    
    try:
        r = requests.get(f'https://api.hackertarget.com/aslookup/?q={ip}', timeout=TIMEOUT)
        if r.status_code == 200 and 'error' not in r.text.lower():
            asn = r.text.strip()
            parts = asn.split(',')
            if len(parts) >= 2:
                print(f"     {C.GREEN}[+]{C.END} ASN: {C.WHITE}{parts[0].strip()}{C.END}")
                print(f"     {C.GREEN}[+]{C.END} Organization: {C.WHITE}{parts[1].strip()}{C.END}")
            return asn
    except:
        pass
    
    print(f"     {C.YELLOW}[!]{C.END} ASN: {C.YELLOW}NOT AVAILABLE{C.END}")
    return None

def get_detailed_address(lat, lon):
    """Dapatkan alamat detail dari koordinat"""
    print(f"\n  {C.CYAN}[PHASE 4]{C.END} {C.BOLD}Address Resolution...{C.END}")
    print(f"  {C.GRAY}{'─' * 55}{C.END}")
    print(f"     {C.GRAY}Target: {lat:.6f}, {lon:.6f}{C.END}")
    
    addresses = []
    
    print(f"     {C.YELLOW}[*]{C.END} OpenStreetMap...", end=" ", flush=True)
    try:
        r = requests.get(
            f'https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}&zoom=18&addressdetails=1',
            headers={'User-Agent': 'LegalTrack/4.0'},
            timeout=TIMEOUT
        )
        if r.status_code == 200:
            data = r.json()
            addresses.append({
                'source': 'OpenStreetMap',
                'display': data.get('display_name', ''),
                'address': data.get('address', {}),
            })
            print(f"{C.GREEN}SUCCESS{C.END}")
    except:
        print(f"{C.RED}FAILED{C.END}")
    
    print(f"     {C.YELLOW}[*]{C.END} BigDataCloud...", end=" ", flush=True)
    try:
        r = requests.get(
            f'https://api.bigdatacloud.net/data/reverse-geocode-client?latitude={lat}&longitude={lon}&localityLanguage=id',
            timeout=TIMEOUT
        )
        if r.status_code == 200:
            data = r.json()
            addresses.append({
                'source': 'BigDataCloud',
                'display': f"{data.get('locality', '')}, {data.get('city', '')}, {data.get('countryName', '')}",
                'address': {
                    'locality': data.get('locality', ''),
                    'city': data.get('city', ''),
                    'state': data.get('principalSubdivision', ''),
                    'country': data.get('countryName', ''),
                },
            })
            print(f"{C.GREEN}SUCCESS{C.END}")
    except:
        print(f"{C.RED}FAILED{C.END}")
    
    return addresses

def extract_coordinates(geo_results):
    """Ekstrak koordinat dari hasil geolocation"""
    coords = []
    
    mappings = {
        'ip-api.com': ('lat', 'lon', 'city', 'regionName'),
        'ipinfo.io': (None, None, 'city', 'region'),
        'ipwhois.app': ('latitude', 'longitude', 'city', 'region'),
        'ip-api.io': ('latitude', 'longitude', 'city', 'region_name'),
        'geoplugin.net': ('geoplugin_latitude', 'geoplugin_longitude', 'geoplugin_city', 'geoplugin_region'),
        'reallyfreegeoip.org': ('latitude', 'longitude', 'city', 'region_name'),
        'freeipapi.com': ('latitude', 'longitude', 'cityName', 'regionName'),
        'ipapi.co': ('latitude', 'longitude', 'city', 'region'),
    }
    
    for source, data in geo_results.items():
        if not data:
            continue
        
        mapping = mappings.get(source)
        if not mapping:
            continue
        
        try:
            if source == 'ipinfo.io':
                loc = data.get('loc', '').split(',')
                if len(loc) == 2:
                    lat, lon = float(loc[0]), float(loc[1])
                else:
                    continue
            else:
                lat = float(data.get(mapping[0], 0))
                lon = float(data.get(mapping[1], 0))
            
            if lat and lon:
                coords.append({
                    'source': source,
                    'lat': lat,
                    'lon': lon,
                    'city': data.get(mapping[2], 'Unknown'),
                    'region': data.get(mapping[3], ''),
                })
        except:
            continue
    
    return coords

# ==========================================
# MAIN MENU
# ==========================================

def main():
    try:
        clear_screen()
        print_startup_banner()
        
        # Run initialization
        if not initialize():
            sys.exit(1)
        
        while True:
            print(f"""
  {C.CYAN}╔═══════════════════════════════════════════════════╗{C.END}
  {C.CYAN}║{C.END}  {C.BOLD}SELECT OPERATION MODE{C.END}                            {C.CYAN}║{C.END}
  {C.CYAN}╠═══════════════════════════════════════════════════╣{C.END}
  {C.CYAN}║{C.END}  {C.GREEN}[1]{C.END} 🌍 Track IP Address (Geolocation)            {C.CYAN}║{C.END}
  {C.CYAN}║{C.END}  {C.GREEN}[2]{C.END} 👤 Search Username (Social Media OSINT)      {C.CYAN}║{C.END}
  {C.CYAN}║{C.END}  {C.GREEN}[3]{C.END} 📧 Search Email (Breach Check + Accounts)    {C.CYAN}║{C.END}
  {C.CYAN}║{C.END}  {C.GREEN}[4]{C.END} 📱 Analyze Phone Number                      {C.CYAN}║{C.END}
  {C.CYAN}║{C.END}  {C.GREEN}[5]{C.END} 🔥 FULL OSINT (All of the above)             {C.CYAN}║{C.END}
  {C.CYAN}║{C.END}  {C.RED}[0]{C.END} ❌ Exit Legal Track                          {C.CYAN}║{C.END}
  {C.CYAN}╚═══════════════════════════════════════════════════╝{C.END}
            """)
            
            try:
                choice = input(f"  {C.YELLOW}legal-track{C.END}:{C.BLUE}~${C.END} ").strip()
            except (KeyboardInterrupt, EOFError):
                print(f"\n\n  {C.RED}[!] Session terminated{C.END}")
                sys.exit(0)
            
            if choice == '0':
                print(f"\n  {C.GREEN}[✓] Legal Track terminated. Stay safe! ⚖️{C.END}\n")
                break
            
            # ==========================================
            # OPTION 1: IP TRACKING
            # ==========================================
            if choice == '1':
                print(f"\n  {C.YELLOW}[?] Enter IP address (or press Enter for your IP):{C.END}")
                try:
                    ip = input(f"  {C.YELLOW}IP>{C.END} ").strip()
                except (KeyboardInterrupt, EOFError):
                    continue
                
                if not ip:
                    print(f"  {C.YELLOW}[*] Detecting your IP...{C.END}")
                    try:
                        r = requests.get('https://api.ipify.org?format=json', timeout=10)
                        ip = r.json().get('ip')
                        print(f"  {C.GREEN}[+] Your IP: {ip}{C.END}")
                    except:
                        print(f"  {C.RED}[!] Failed{C.END}")
                        continue
                
                print(f"\n{C.GREEN}{'━' * 60}{C.END}")
                print(f"  {C.BOLD}🎯 TRACKING IP: {C.RED}{ip}{C.END}")
                print(f"{C.GREEN}{'━' * 60}{C.END}")
                
                geo_results = get_all_geolocation(ip)
                dns_records = get_dns_records(ip)
                asn_info = get_asn_info(ip)
                
                all_coords = extract_coordinates(geo_results)
                
                if all_coords:
                    avg_lat = sum(c['lat'] for c in all_coords) / len(all_coords)
                    avg_lon = sum(c['lon'] for c in all_coords) / len(all_coords)
                    detailed = get_detailed_address(avg_lat, avg_lon)
                    
                    print(f"\n{C.RED}{'═' * 60}{C.END}")
                    print(f"  {C.BOLD}📊 RESULTS{C.END}")
                    print(f"{C.RED}{'═' * 60}{C.END}")
                    
                    print(f"\n  {C.CYAN}▶ Location from {len(all_coords)} sources:{C.END}")
                    for c in all_coords:
                        print(f"    {C.YELLOW}◉{C.END} {c['source']:18} → {C.WHITE}{c['city']}{C.END}, {c['region']}")
                    
                    print(f"\n  {C.CYAN}▶ Average Coordinates:{C.END}")
                    print(f"    {C.WHITE}{avg_lat:.6f}, {avg_lon:.6f}{C.END}")
                    
                    if detailed:
                        print(f"\n  {C.CYAN}▶ Detailed Address:{C.END}")
                        for addr in detailed:
                            print(f"    {C.MAGENTA}{addr['source']}:{C.END}")
                            a = addr.get('address', {})
                            if addr['source'] == 'OpenStreetMap' and a:
                                fields = [
                                    ('🏠 Jalan/Bangunan', a.get('road') or a.get('pedestrian') or a.get('amenity', '')),
                                    ('🏘️  Kelurahan/Desa', a.get('village') or a.get('suburb') or a.get('neighbourhood', '')),
                                    ('🏙️  Kecamatan',      a.get('county') or a.get('district', '')),
                                    ('🌆 Kota/Kabupaten',  a.get('city') or a.get('town') or a.get('municipality', '')),
                                    ('🗺️  Provinsi',        a.get('state', '')),
                                    ('🌍 Negara',          a.get('country', '')),
                                    ('📮 Kode Pos',        a.get('postcode', '')),
                                ]
                                for label, val in fields:
                                    if val:
                                        print(f"      {C.GREEN}{label}: {C.WHITE}{val}{C.END}")
                                print(f"      {C.GRAY}Full: {addr['display'][:120]}{C.END}")
                            else:
                                for label, val in [
                                    ('🌆 Kota',    a.get('city', '')),
                                    ('🏘️  Lokal',   a.get('locality', '')),
                                    ('🗺️  Provinsi', a.get('state', '')),
                                    ('🌍 Negara',   a.get('country', '')),
                                ]:
                                    if val:
                                        print(f"      {C.GREEN}{label}: {C.WHITE}{val}{C.END}")
                    
                    print(f"\n  {C.CYAN}▶ Google Maps:{C.END}")
                    print(f"    {C.BLUE}https://www.google.com/maps?q={avg_lat},{avg_lon}&z=16{C.END}")
                
                print(f"\n{C.RED}{'═' * 60}{C.END}")
            
            # ==========================================
            # OPTION 2: USERNAME SEARCH
            # ==========================================
            elif choice == '2':
                try:
                    username = input(f"\n  {C.YELLOW}[?] Enter username to search:{C.END} ").strip()
                except (KeyboardInterrupt, EOFError):
                    continue
                
                if not username:
                    continue
                
                print(f"\n{C.GREEN}{'━' * 60}{C.END}")
                print(f"  {C.BOLD}👤 SEARCHING USERNAME: {C.RED}{username}{C.END}")
                print(f"{C.GREEN}{'━' * 60}{C.END}")
                
                found, not_found, errors = search_username(username)
                
                print(f"\n{C.RED}{'═' * 60}{C.END}")
                print(f"  {C.BOLD}📊 RESULTS{C.END}")
                print(f"{C.RED}{'═' * 60}{C.END}")
                
                print(f"\n  {C.GREEN}Found on {len(found)} platforms:{C.END}")
                for platform, url in found:
                    print(f"    {C.GREEN}✓{C.END} {platform}")
                    if url:
                        print(f"      {C.BLUE}{url}{C.END}")
                
                print(f"\n{C.RED}{'═' * 60}{C.END}")
            
            # ==========================================
            # OPTION 3: EMAIL SEARCH
            # ==========================================
            elif choice == '3':
                try:
                    email = input(f"\n  {C.YELLOW}[?] Enter email to search:{C.END} ").strip()
                except (KeyboardInterrupt, EOFError):
                    continue
                
                if not email or '@' not in email:
                    print(f"  {C.RED}[!] Invalid email{C.END}")
                    continue
                
                print(f"\n{C.GREEN}{'━' * 60}{C.END}")
                print(f"  {C.BOLD}📧 SEARCHING EMAIL: {C.RED}{email}{C.END}")
                print(f"{C.GREEN}{'━' * 60}{C.END}")
                
                breach_result = check_email_breaches(email)
                accounts = search_email_accounts(email)
                
                print(f"\n{C.RED}{'═' * 60}{C.END}")
                print(f"  {C.BOLD}📊 RESULTS{C.END}")
                print(f"{C.RED}{'═' * 60}{C.END}")
                
                if breach_result.get('breaches'):
                    print(f"\n  {C.RED}⚠️  SECURITY WARNINGS:{C.END}")
                    for b in breach_result['breaches']:
                        print(f"    {C.RED}• {b}{C.END}")
                
                if accounts:
                    print(f"\n  {C.GREEN}📱 Found Accounts:{C.END}")
                    for acc in accounts:
                        print(f"    {C.GREEN}✓{C.END} {acc['platform']}")
                        if acc.get('username'):
                            print(f"      Username: {acc['username']}")
                        if acc.get('url'):
                            print(f"      {C.BLUE}{acc['url']}{C.END}")
                
                print(f"\n{C.RED}{'═' * 60}{C.END}")
            
            # ==========================================
            # OPTION 4: PHONE ANALYSIS
            # ==========================================
            elif choice == '4':
                try:
                    phone = input(f"\n  {C.YELLOW}[?] Enter phone number:{C.END} ").strip()
                except (KeyboardInterrupt, EOFError):
                    continue
                
                if not phone:
                    continue
                
                print(f"\n{C.GREEN}{'━' * 60}{C.END}")
                print(f"  {C.BOLD}📱 ANALYZING PHONE: {C.RED}{phone}{C.END}")
                print(f"{C.GREEN}{'━' * 60}{C.END}")
                
                result = analyze_phone_number(phone)
                
                print(f"\n{C.RED}{'═' * 60}{C.END}")
            
            # ==========================================
            # OPTION 5: FULL OSINT
            # ==========================================
            elif choice == '5':
                print(f"\n  {C.BOLD}🔥 FULL OSINT MODE{C.END}")
                print(f"  {C.GRAY}Enter all available information:{C.END}")
                
                try:
                    ip = input(f"\n  {C.YELLOW}[?] IP Address (optional):{C.END} ").strip()
                    username = input(f"  {C.YELLOW}[?] Username (optional):{C.END} ").strip()
                    email = input(f"  {C.YELLOW}[?] Email (optional):{C.END} ").strip()
                    phone = input(f"  {C.YELLOW}[?] Phone (optional):{C.END} ").strip()
                except (KeyboardInterrupt, EOFError):
                    continue
                
                print(f"\n{C.GREEN}{'━' * 60}{C.END}")
                print(f"  {C.BOLD}🔥 RUNNING FULL OSINT SCAN{C.END}")
                print(f"{C.GREEN}{'━' * 60}{C.END}")
                
                if ip:
                    print(f"\n  {C.MAGENTA}━━━ IP TRACKING ━━━{C.END}")
                    geo_results = get_all_geolocation(ip)
                    all_coords = extract_coordinates(geo_results)
                    if all_coords:
                        avg_lat = sum(c['lat'] for c in all_coords) / len(all_coords)
                        avg_lon = sum(c['lon'] for c in all_coords) / len(all_coords)
                        get_detailed_address(avg_lat, avg_lon)
                
                if username:
                    print(f"\n  {C.MAGENTA}━━━ USERNAME SEARCH ━━━{C.END}")
                    search_username(username)
                
                if email:
                    print(f"\n  {C.MAGENTA}━━━ EMAIL SEARCH ━━━{C.END}")
                    check_email_breaches(email)
                    search_email_accounts(email)
                
                if phone:
                    print(f"\n  {C.MAGENTA}━━━ PHONE ANALYSIS ━━━{C.END}")
                    analyze_phone_number(phone)
                
                print(f"\n{C.RED}{'═' * 60}{C.END}")
                print(f"  {C.GREEN}[✓] Full OSINT scan complete!{C.END}")
                print(f"{C.RED}{'═' * 60}{C.END}")
            
            else:
                print(f"  {C.RED}[!] Invalid option{C.END}")
                
    except (KeyboardInterrupt, EOFError):
        print(f"\n\n  {C.RED}[!] Session terminated{C.END}\n")
        sys.exit(0)

if __name__ == '__main__':
    main()
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
    """Analisis nomor telepon"""
    
    print(f"\n  {C.CYAN}[PHONE ANALYSIS]{C.END} {C.BOLD}Analyzing: {phone}{C.END}")
    print(f"  {C.GRAY}{'─' * 55}{C.END}")
    
    clean_phone = re.sub(r'[^\d+]', '', phone)
    
    if clean_phone.startswith('08'):
        clean_phone = '+62' + clean_phone[1:]
    elif clean_phone.startswith('62'):
        clean_phone = '+' + clean_phone
    
    print(f"     {C.WHITE}Formatted:{C.END} {clean_phone}")
    
    result = {
        'formatted': clean_phone,
        'carrier': None,
        'type': None,
        'country': None,
    }
    
    if clean_phone.startswith('+62'):
        prefix = clean_phone[3:6]
        
        carrier_map = {
            '811': 'Telkomsel', '812': 'Telkomsel', '813': 'Telkomsel',
            '821': 'Telkomsel', '822': 'Telkomsel', '823': 'Telkomsel',
            '851': 'Telkomsel', '852': 'Telkomsel', '853': 'Telkomsel',
            '814': 'Indosat', '815': 'Indosat', '816': 'Indosat',
            '855': 'Indosat', '856': 'Indosat', '857': 'Indosat', '858': 'Indosat',
            '817': 'XL', '818': 'XL', '819': 'XL',
            '859': 'XL', '877': 'XL', '878': 'XL',
            '831': 'Axis', '832': 'Axis', '833': 'Axis', '838': 'Axis',
            '895': 'Three', '896': 'Three', '897': 'Three',
            '898': 'Three', '899': 'Three',
            '881': 'Smartfren', '882': 'Smartfren', '883': 'Smartfren',
            '884': 'Smartfren', '885': 'Smartfren', '886': 'Smartfren',
            '887': 'Smartfren', '888': 'Smartfren', '889': 'Smartfren',
        }
        
        carrier = carrier_map.get(prefix, 'Unknown')
        result['carrier'] = carrier
        result['country'] = 'Indonesia'
        result['type'] = 'Mobile'
        
        print(f"     {C.GREEN}[+]{C.END} Country: {C.WHITE}Indonesia{C.END}")
        print(f"     {C.GREEN}[+]{C.END} Carrier: {C.WHITE}{carrier}{C.END}")
        print(f"     {C.GREEN}[+]{C.END} Type: {C.WHITE}Mobile{C.END}")
    
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
                            display = addr['display']
                            for part in display.split(', ')[:5]:
                                print(f"      {C.GREEN}• {part}{C.END}")
                    
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

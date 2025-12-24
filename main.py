"""
IP Location Tracker - Backend Server
Menggunakan Flask untuk serve web dan API geolocation
"""

from flask import Flask, render_template, jsonify, request
import requests
import json

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    """Halaman utama"""
    return render_template('index.html')

@app.route('/api/locate', methods=['POST'])
def locate_ip():
    """API endpoint untuk melacak IP"""
    data = request.get_json()
    ip_address = data.get('ip', '')
    
    if not ip_address:
        return jsonify({'error': 'IP address diperlukan'}), 400
    
    try:
        # Menggunakan ip-api.com (gratis, tanpa API key)
        response = requests.get(f'http://ip-api.com/json/{ip_address}?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query')
        location_data = response.json()
        
        if location_data.get('status') == 'fail':
            return jsonify({'error': location_data.get('message', 'IP tidak valid atau tidak ditemukan')}), 400
        
        return jsonify({
            'success': True,
            'data': {
                'ip': location_data.get('query'),
                'country': location_data.get('country'),
                'country_code': location_data.get('countryCode'),
                'region': location_data.get('regionName'),
                'city': location_data.get('city'),
                'zip': location_data.get('zip'),
                'latitude': location_data.get('lat'),
                'longitude': location_data.get('lon'),
                'timezone': location_data.get('timezone'),
                'isp': location_data.get('isp'),
                'org': location_data.get('org'),
                'as': location_data.get('as')
            }
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/my-ip')
def get_my_ip():
    """Mendapatkan IP pengunjung"""
    # Cek header X-Forwarded-For untuk reverse proxy
    if request.headers.get('X-Forwarded-For'):
        ip = request.headers.get('X-Forwarded-For').split(',')[0].strip()
    else:
        ip = request.remote_addr
    
    return jsonify({'ip': ip})

if __name__ == '__main__':
    print("🌐 IP Location Tracker Server")
    print("📍 Buka http://localhost:5000 di browser")
    app.run(debug=True, host='0.0.0.0', port=5000)

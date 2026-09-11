import json
import requests
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # CoinGecko reliable API with User-Agent header
            url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
            headers = {'User-Agent': 'Mozilla/5.0'}
            
            response = requests.get(url, headers=headers, timeout=10)
            data = response.json()
            
            btc_price = data.get("bitcoin", {}).get("usd", "N/A")
            
            result = {
                "status": "success",
                "coin": "Bitcoin (BTC)",
                "price_usd": btc_price
            }
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(result).encode('utf-8'))
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_msg = {"status": "error", "message": str(e)}
            self.wfile.write(json.dumps(error_msg).encode('utf-8'))
        return

import requests
from http.server import BaseHTTPRequestHandler

URL = "https://freefirenation.com/wp-admin/admin-ajax.php"

HEADERS = {
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "x-requested-with": "XMLHttpRequest",
    "origin": "https://freefirenation.com",
    "referer": "https://freefirenation.com/free-fire-id-check/",
    "user-agent": "Mozilla/5.0"
}

COOKIE = "dom3ic8zudi28v8lr6fgphwffqoz0j6c=62d8e56f-b3e1-41e3-9b2e-a9c1073f4fcc:2:1"


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            import urllib.parse as up

            query = up.urlparse(self.path).query
            params = up.parse_qs(query)

            uid = params.get("uid", [None])[0]
            region = params.get("region", ["ind"])[0]
            nonce = params.get("nonce", [None])[0]

            if not uid or not nonce:
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(b'{"success":false,"error":"uid or nonce missing"}')
                return

            data = {
                "action": "ff_get_player_info_paid",
                "uid": uid,
                "region": region,
                "nonce": nonce
            }

            res = requests.post(
                URL,
                headers=HEADERS,
                cookies={"cookie": COOKIE},
                data=data,
                timeout=15
            )

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(res.content)

        except Exception as e:
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(str(e).encode())
    try:
        res = requests.post(
            URL,
            headers=HEADERS,
            cookies={"cookie": COOKIE},
            data=data,
            timeout=15
        )

        return res.json()

    except Exception as e:
        return {"success": False, "error": str(e)}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

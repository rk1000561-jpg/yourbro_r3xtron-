from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

URL = "https://freefirenation.com/wp-admin/admin-ajax.php"

HEADERS = {
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "x-requested-with": "XMLHttpRequest",
    "origin": "https://freefirenation.com",
    "referer": "https://freefirenation.com/free-fire-id-check/",
    "user-agent": "Mozilla/5.0"
}

COOKIE = "dom3ic8zudi28v8lr6fgphwffqoz0j6c=62d8e56f-b3e1-41e3-9b2e-a9c1073f4fcc:2:1"

@app.route("/")
def home():
    return {"status": "API running", "owner": "shiv"}

@app.route("/api")
def get_uid():
    uid = request.args.get("uid")
    region = request.args.get("region", "ind")
    nonce = request.args.get("nonce")

    if not uid or not nonce:
        return jsonify({"success": False, "error": "uid or nonce missing"})

    data = {
        "action": "ff_get_player_info_paid",
        "uid": uid,
        "region": region,
        "nonce": nonce
    }

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

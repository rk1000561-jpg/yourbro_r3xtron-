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


# ⚡ MAIN SIMPLE ENDPOINT
@app.route("/api")
def get_profile():
    uid = request.args.get("uid")

    if not uid:
        return jsonify({"success": False, "error": "uid required"})

    # ⚠️ NOTE: static nonce (demo purpose)
    # real production me dynamic nonce chahiye hota hai
    nonce = "2d79f616a1"

    data = {
        "action": "ff_get_player_info_paid",
        "uid": uid,
        "region": "ind",
        "nonce": nonce
    }

    try:
        res = requests.post(
            URL,
            headers=HEADERS,
            cookies={"cookie": COOKIE},
            data=data
        )

        return jsonify(res.json())

    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


@app.route("/")
def home():
    return jsonify({
        "status": "running",
        "usage": "/api?uid=YOUR_ID"
    })


handler = app

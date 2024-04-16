from flask import Blueprint, render_template
from flask_login import login_required, current_user
from flask import request, jsonify
import requests
import os
views = Blueprint("views", __name__)
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY", "")
API_URL = "https://prodapi.phot.ai/external/api/v2/user_activity/color-restoration-2k/"

def colorize_image(image_url, filename):
    headers = {"x-api-key": API_KEY, "Content-Type": "application/json"}
    data = {"fileName": filename, "sourceUrl": image_url}

    response = requests.post(API_URL, headers=headers, json=data)

    # print(response.json()["data"]['2k']['url'], "response")

    print(response.json(), "response")
    if response.status_code == 200:
        return response.json()
    else:
        return response.json()

@views.route("/", methods=['GET', 'POST'])
@login_required
def home():
    if request.method == "POST":
        if "image_url" not in request.form:
            return jsonify({"error": "No image URL provided"}), 400
        if "filename" not in request.form:
            return jsonify({"error": "No filename provided"}), 400

        image_url = request.form["image_url"]
        filename = request.form["filename"]

        res = colorize_image(image_url, filename)

        errors = ""
        colored_image_url = ""

        if "message" in res:
            errors = res["message"]
        else:
            colored_image_url = res.get("data", {}).get("2k", {}).get("url")

        if colored_image_url:
            return render_template("Home.html", colored_image_url=colored_image_url, user=current_user)
        else:
            return render_template("Home.html", errors=errors, user=current_user)
        
    return render_template("Home.html", user=current_user)

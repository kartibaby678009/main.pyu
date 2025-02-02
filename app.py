import os
import time
import requests
import schedule
from flask import Flask, request, render_template_string
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# HTML & CSS Combined in Flask
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Facebook Auto Comment Bot</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background-color: #f4f4f4;
        }
        form {
            background: white;
            padding: 20px;
            width: 300px;
            margin: auto;
            border-radius: 5px;
            box-shadow: 0px 0px 10px gray;
        }
        input, button {
            display: block;
            width: 100%;
            margin: 10px 0;
            padding: 10px;
        }
        button {
            background: blue;
            color: white;
            border: none;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h1>Facebook Auto Comment Bot</h1>
    <form action="/" method="post">
        <label>Access Token:</label>
        <input type="text" name="token" required>
        
        <label>Post Link:</label>
        <input type="text" name="post_link" required>

        <label>Comment Time (HH:MM AM/PM):</label>
        <input type="text" name="time" placeholder="10:30 AM" required>

        <label>Haters List (Comma-separated):</label>
        <input type="text" name="haters" placeholder="Hater1, Hater2, Hater3">

        <button type="submit">Save & Schedule</button>
    </form>
</body>
</html>
"""

DATA_FILE = "data.txt"

# Function to post a comment on Facebook
def post_comment():
    if not os.path.exists(DATA_FILE):
        print("❌ No scheduled comment found.")
        return
    
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = dict(line.strip().split("=", 1) for line in file if "=" in line)

    token = data.get("TOKEN")
    post_link = data.get("POST_LINK")
    comment_text = "This is an auto-generated comment using Flask!"

    if not token or not post_link:
        print("❌ Error: Missing Token or Post Link")
        return

    # Extract Post ID from the link
    post_id = post_link.split("/")[-1]

    # Facebook Graph API Call
    url = f"https://graph.facebook.com/{post_id}/comments"
    params = {
        "message": comment_text,
        "access_token": token
    }

    response = requests.post(url, params=params)

    if response.status_code == 200:
        print("✅ Comment posted successfully on Facebook!")
    else:
        print(f"❌ Failed to post comment: {response.text}")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        token = request.form.get("token")
        post_link = request.form.get("post_link")
        time_set = request.form.get("time")
        haters = request.form.get("haters", "")

        if not token or not post_link or not time_set:
            return "❌ Error: Missing required fields."

        # Save data to `data.txt`
        data_content = f"TOKEN={token}\nTIME={time_set}\nPOST_LINK={post_link}\nHATERS={haters}"
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            file.write(data_content)

        # Schedule the comment
        schedule.every().day.at(time_set).do(post_comment)

        return "✅ Data saved & comment scheduled successfully!"

    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    app.run(debug=True)

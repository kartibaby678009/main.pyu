import os

# 🟢 Step 1: Data File Create Karna
data_file = "data.txt"
data_content = """TOKEN=YourAccessTokenHere
TIME=10:30 AM
POST_LINK=https://facebook.com/your-post-link-here
HATERS=Hater1, Hater2, Hater3
"""

with open(data_file, "w", encoding="utf-8") as file:
    file.write(data_content)
print(f"{data_file} created successfully!")

# 🟢 Step 2: HTML Form Generate Karna
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Auto Comment Bot</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Facebook Auto Comment Bot</h1>
    <form action="#" method="post">
        <label>Access Token:</label>
        <input type="text" name="token" required>
        
        <label>Time:</label>
        <input type="text" name="time" placeholder="HH:MM AM/PM" required>
        
        <label>Post Link:</label>
        <input type="text" name="post_link" required>

        <label>Haters List:</label>
        <input type="text" name="haters" placeholder="Comma-separated names" required>
        
        <button type="submit">Submit</button>
    </form>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as file:
    file.write(html_content)
print("index.html created successfully!")

# 🟢 Step 3: CSS File Generate Karna
css_content = """body {
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
"""

with open("style.css", "w", encoding="utf-8") as file:
    file.write(css_content)
print("style.css created successfully!")

print("✅ All files are ready! Upload to GitHub & Deploy on Render.")

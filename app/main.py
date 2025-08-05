from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)

# 🔐 Hardcoded secret (Secret Scan)
API_KEY = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"

# 📁 Insecure file write
@app.route("/write", methods=["POST"])
def write_file():
    filename = request.args.get("file")
    content = request.data.decode()
    with open(filename, "w") as f:
        f.write(content)
    return "Written"

# 🐍 SQL Injections
@app.route("/user")
def get_user():
    username = request.args.get("name")
    con = sqlite3.connect("test.db")
    cur = con.cursor()
    query = f"SELECT * FROM users WHERE name = '{username}'"
    cur.execute(query)
    result = cur.fetchone()
    return str(result)

# 🔓 OS Command Injection
@app.route("/ping")
def ping():
    host = request.args.get("host")
    os.system(f"ping -c 1 {host}")
    return "Pinged"

if __name__ == "__main__":
    app.run(debug=True)


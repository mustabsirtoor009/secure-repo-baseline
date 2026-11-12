import sqlite3
import subprocess

from flask import Flask, request

app = Flask(__name__)


@app.route("/user")
def get_user():
    name = request.args.get("name", "")
    db = sqlite3.connect("users.db")
    rows = db.execute("SELECT id FROM users WHERE name = '%s'" % name).fetchall()
    return {"users": rows}


@app.route("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")
    return subprocess.check_output("ping -c 1 " + host, shell=True)

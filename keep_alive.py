from flask import Flask
from threading import Thread
import os
from utils import log_error

app = Flask('')

@app.route('/')
def home():
    log_error("ping received")
    return "Bot is alive!"

def run():
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000)),
        debug=False,
        use_reloader=False
    )
def keep_alive():
    t = Thread(target=run)
    t.start()
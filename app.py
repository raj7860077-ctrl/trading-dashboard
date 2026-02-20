from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def dashboard():
    signal = random.choice(["BUY", "SELL", "NO TRADE"])
    entry = 22500
    sl = 22450
    target = 22600
    rr = round((target-entry)/(entry-sl),2)

    return render_template("dashboard.html",
                           signal=signal,
                           entry=entry,
                           sl=sl,
                           target=target,
                           rr=rr)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

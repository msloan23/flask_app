
import weather2
from flask import Flask, render_template, request
app = Flask(__name__)
import os

@app.route("/")
def index():
    address = request.values.get('address')
    forecast = None
    if address:
        forecast = weather2.get_weather(address)
    return render_template('index.html', forecast=forecast)

@app.route('/about')
def about():
	return render_template('about.html')

if __name__ == "__main__":
	port = int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0", port=port)
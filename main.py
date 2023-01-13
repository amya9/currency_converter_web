import requests
from flask import Flask, request, render_template

app = Flask(__name__)

# Set up the route for the home page
@app.route("/")
def home():
    # Get the list of available currencies from the API
    currencies = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()["rates"]
    # Render the home template, passing in the list of currencies
    return render_template("home.html", currencies=currencies)

# Set up the route for the conversion page
@app.route("/convert", methods=["POST"])
def convert():
    # Get the amount and currencies from the form
    amount = request.form["amount"]
    from_currency = request.form["from_currency"]
    to_currency = request.form["to_currency"]

    # Make a request to the API to get the conversion rate
    rate = requests.get(f"https://api.exchangerate-api.com/v4/latest/{from_currency}").json()["rates"][to_currency]

    # Calculate the converted amount
    converted_amount = float(amount) * rate

    # Render the conversion template, passing in the original amount, the converted amount, and the conversion rate
    return render_template("convert.html", amount=amount, converted_amount=converted_amount, rate=rate)

if __name__ == "__main__":
    app.run(debug=True , port= 5018 , use_reloader=True )
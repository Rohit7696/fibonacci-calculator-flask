from flask import Flask, render_template, request
import os

app = Flask(__name__)

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

@app.route("/", methods=["GET", "POST"])
def index():
    result = []
    if request.method == "POST":
        try:
            num = int(request.form["number"])
            if num < 0:
                result = ["Please enter a positive number."]
            else:
                result = fibonacci(num)
        except ValueError:
            result = ["Invalid input. Please enter a number."]
    return render_template("index.html", result=result)

if __name__ == "__main__":
    # Use the environment's PORT variable, defaulting to 5000 if not set
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)

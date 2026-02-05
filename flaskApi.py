from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route("/about")
def about():
    return "This is the about page"

@app.route("/contact")
def contact():
    return "This is the contact page"

@app.route("/contact/<name>")
def user(name):
    return f"Hello {name}, call us at 305-954-2626"

if __name__ == "__main__":
    app.run(debug=True)


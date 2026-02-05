from flask import Flask, jsonify

app = Flask(__name__)

DATA = [
    {
        "id":1,
        "campus":"MMC",
        "lat":25.76,
        "long":-80.36,
    }, {
        "id":2,
        "campus":"BBC",
        "lat":25.90,
        "long":-80.13,
    },
       {
        "id":3,
        "campus":"DC",
        "lat":38.89,
        "long":-77.01,
    },
]

@app.route("/")
def index():
    return """
    <h1>FIU Campuses API</h1>
    <p>Try these endpoints</p>
    <ul>
    <li><a href="/api/health">health page</a></li>
    <li><a href="/api/items">items page</a></li>
    <li><a href="/api/items/1">item1 page</a></li>
    </ul>
    """

@app.route("/api/health")
def health():
    return jsonify({"status":"ok"}), 200

@app.route("/api/items")
def items():
    return jsonify(DATA), 200

@app.route("/api/items/<int:id>")
def item(id):
    for i in DATA: 
        if i["id"]==id:
            return jsonify(i), 200
    return jsonify({"error":"item not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
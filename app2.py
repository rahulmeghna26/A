# If port Error Failed Then Add This
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "This is YMusic-UserBot"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)  # Modified this line

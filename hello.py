from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello github"
@app.route("/index")
def index():
    return "This is index"
if __name__ == "__main__":
    app.run()

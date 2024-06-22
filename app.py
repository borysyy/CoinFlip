from flask import Flask, render_template, redirect, request, session, flash
from flask_session import Session


# Create the flask app
app = Flask(__name__)

# Create the seesion
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_FILE_DIR"] = "./flask_session_cache"
Session(app)


@app.route("/")
def index():
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
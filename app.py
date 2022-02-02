from flask import Flask, render_template
app = Flask(__name__)
# heroes = {
#     "player": player,
#     "enemy": enemy
# }

@app.route("/")
def menu():
    return render_template("index.html")

@app.route("/choose-hero/")
def hero_page():
    return render_template ("hero_chosing.html")


if __name__ == "__main__":
    app.run(port=8000)
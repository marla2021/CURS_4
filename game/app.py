from game.equipment import EquipmentData
from flask import Flask, render_template
from game.utils import load_equipment
app = Flask(__name__)
# heroes = {
#     "player": player,
#     "enemy": enemy
# }

EQUIPMENT: EquipmentData = load_equipment()


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/choose-hero", methods=["GET", "POST"])
def choose_hero():
    if request.method == "GET":
        return render_template("hero_chosing.html",
                               header ="Выберите героя",
                               classes=pers_classes.values(),
                               equipment=Equipment,
                               next_button="Начать сражение")




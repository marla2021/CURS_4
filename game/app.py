from equipment import EquipmentData
from flask import Flask, render_template, request, redirect, url_for
from utils import load_equipment
from typing import Dict
from unit import Hero
from classes import UnitClass
from arena import Game


app = Flask(__name__)
app.url_map.strict_slashes = False

heroes: Dict[str, Hero] = dict()

EQUIPMENT: EquipmentData = load_equipment()


def render_choose_pers_template(**kwargs) -> str:
    return render_template("hero_choosing.html",
                           classes = personage_classes.values(),
                           equipment = EQUIPMENT,
                           **kwargs,)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/choose-hero", methods=["GET", "POST"])
def choose_hero():
    if request.method == "GET":
        return render_template("hero_choosing.html",
                               header ="Выберите героя",
                               classes=pers_classes.values(),
                               equipment=Equipment,
                               next_button="Начать сражение")
    heroes["player"] = Player(unit_class= pers_classes[request.form["unit_class"]],
                              weapon = EQUIPMENT.get_weapon(request.form["weapon"]),
                              armor = EQUIPMENT.get_weapon(request.form["armor"]),
                              name = request.form["name"])
    return redirect(url_for("choose_enemy"))


@app.route("/choose-enemy", methods=["GET", "POST"])
def choose_enemy():
    if request.method == "GET":
        return render_template("hero_choosing.html",
                               header ="Выберите врага",
                               classes=pers_classes.values(),
                               equipment=Equipment,
                               next_button="Начать сражение")
    heroes["enemy"] = Enemy(unit_class= pers_classes[request.form["unit_class"]],
                              weapon = EQUIPMENT.get_weapon(request.form["weapon"]),
                              armor = EQUIPMENT.get_weapon(request.form["armor"]),
                              name = request.form["name"])
    return redirect(url_for("choose_enemy"))


@app.route("/fight")
def start_fight():
    if "player" in heroes and "enemy" in heroes:
        game.run(**heroes)
        return render_template("fight.html", heroes=heroes, result="Битва!")
    return redirect(url_for("index"))


@app.route("/fight/hit")
def hit():
    return render_template("fight.html", heroes=heroes, result=game.player_hit())


@app.route("/fight/use-skill")
def use_skill():
    return render_template("fight.html", heroes=heroes, result=game.player_use_skill())


@app.route("/fight/pass_turn")
def pass_turn():
    return render_template("fight.html", heroes=heroes, result=game.next_move())


@app.route("/fight/end-fight")
def end_fight():
    return redirect(url_for("index"))


# if __name__ == "__main__":
#     app.run()
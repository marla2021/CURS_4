from dataclasses import dataclass


@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: ConcreteSkill

Warrior = UnitClass(
    name = "Воин",
    max_health = 60.0,
    max_stamina = 30.0,
    attack = 0.8,
    stamina = 0.9,
    armor = 1.2,
    skill = None

Thief = UnitClass(
    name = "Вор",
    max_health = 50.0,
    max_stamina = 25.0,
    attack = 1.5,
    stamina = 1.2,
    armor = 1,
    skill = None


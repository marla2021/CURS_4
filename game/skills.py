from abc import ABC, abstractmethod

@dataclass
class Skill():
    name:str
    stamina:float
    damage:float


kick = Skill(name="Свирепый пинок", damage=22, stamina=6)
thust= Skill(name="Мощный укол", damage=15, stamina=5)
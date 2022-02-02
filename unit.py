from abc import ABC


class BaseUnit(ABC):
    def __init__(self, name, cls_unit, hp, stamina, armor, skill):
        self.name = name
        self.cls_unit = cls_unit
        self.hp = hp
        self.stamina = stamina
        self.armor = armor
        self.skill = True
# '''снарядить персонажа оружием — в качестве 
# аргумента принимает оружие и присваивает это 
# оружие свойству экземпляра класса'''
    def equip_weapons(self):
        pass
# снарядить персонажа броней — аналогично для брони;
    def equip_armor(self):
        pass
# приватный метод, вычисляющий итоговый урон,
# здесь можно также заложить логику вычисления выносливости;
    def _damage(self):
        pass
# метод, рассчитывающий получение урона персонажем,
# этот метод не будет являться приватным,
# т.к. он используется классом Умение;
    def get_damage(self):
        pass
# метод, применяющий умение к цели;
    def skill_to_target(self):
        pass
# 1 абстрактный метод — нанести удар
    @abstractmethod
    def strike(self):
        pass
from abc import ABC, abstractmethod


class Skill(ABC):
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def stamina(self):
        pass

    @abstractmethod
    def damage(self):
        pass

    @abstractmethod
    def skill_effect(self):
        pass
    
    
    def use(self, user, target):
        self.user = user
        self.target = target
       
# 練習物件導向

class Npc:
    def __init__(self, name, hp, power, defense):
        self.name = name
        self.hp = hp
        self.power = power
        self.defense = defense

    def damage(self, power):
        damage = power - self.defense
        return damage


class Badass(Npc):
    # 爛招
    def dirty_move(self):
        print(f"{self.name}: I'm using dirty move")

    # 發呆
    def zone_out(self):
        print(f'{self.name}: what? I just zone out,...')



class Hero(Npc):
    # 補血
    def refill_hp(self, cur_hp):
        self.hp = cur_hp + 10
        print(f"{self.name}'s hp is refilled of 10 ==> {self.hp}")

    # 發呆
    def zone_out(self):
        print(f'{self.name}: what? I just zone out,...')
# 練習物件導向
#


class Badass:
    def __init__(self, name, blood, power):
        self.name = name
        self.blood = blood
        self.power = power

    def dirty_move(self):
        print("I'm bad bad")



class Hero:
    def __init__(self, name, blood, power, defense):
        self.name = name
        self.blood = blood
        self.power = power
        self.defense = defense

    # 設定Hero的功能，發出狀聲詞
    def kick_ass(self):
        print('kick~!')

    # 防禦
    def hold_still(self):
        print('nothing hurt!')
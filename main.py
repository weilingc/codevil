from world import Badass, Hero
from random import choice

# 在這個平台中，創建數個Badass類別的物件
corp_cop = Badass('corp_cop', 50, 5)
bad_cop = Badass('bad_cop', 100, 10)
kingpin = Badass('kingpin', 800, 30)

# 在這個平台中，創建數個Hero類別的物件
darevil = Hero('darevil', 600, 20, 5)
elek = Hero('elek', 450, 30, 3)


# Hero和Badass的對決，每一回合一對一，上場選手隨機
team_hero = [darevil, elek]
team_bad = [corp_cop, bad_cop, kingpin]

fight_round = 1
while True:
    team_hero_blood = elek.blood + darevil.blood
    team_bad_blood = bad_cop.blood + corp_cop.blood + kingpin.blood
    if len(team_hero) == 0:
        print('Hero is dead')
        break
    elif len(team_bad) == 0:
        print('badass is dead')
        break

    # 設定打鬥的場景
    else:
        print('-------------------- round', fight_round, '--------------------')
        fight_round += 1

        bad_one = choice(team_bad)
        hero_one = choice(team_hero)

        bad_one.blood -= hero_one.power
        print('Bad side: ',bad_one.name, bad_one.blood, 'total:', team_bad_blood)

        hero_one.blood -= bad_one.power
        print('Hero side: ',hero_one.name, hero_one.blood,  'total:', team_hero_blood )

        if bad_one.blood <= 0:
            team_bad.remove(bad_one)
        elif hero_one.blood <= 0:
            team_hero.remove(hero_one)
        print('壞人數:', len(team_bad), '英雄數:', len(team_hero))











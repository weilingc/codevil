from world import Badass, Hero
from random import choice
from time import sleep
import datetime
import os

# 在這個平台中，創建數個Badass類別的物件
corp_cop = Badass('Corp_cop', 50, 45, 5)
bad_cop = Badass('Bad_cop', 80, 40, 5)
kingpin = Badass('Kingpin', 250, 90, 20)

# 在這個平台中，創建數個Hero類別的物件
darevil = Hero('Darevil', 200, 90, 10)
elek = Hero('Elek', 150, 90, 10)


# Hero和Badass的對決，每一回合一對一，上場選手隨機
team_hero = [darevil, elek]
team_bad = [corp_cop, bad_cop, kingpin]

fight_round = 1
print('現在時間: ',datetime.datetime.now())


while True:
    print('-------------------- round', fight_round, '--------------------')
    fight_round += 1

    # 兩隊各派出一人出來對戰
    bad_one = choice(team_bad)
    hero_one = choice(team_hero)

    # -------------- team_bad 採取動作 --------------
    hero_one.hp -= hero_one.damage(bad_one.power)  # hero扣掉自身防禦值後的傷害值
    move_choice = choice([bad_one.dirty_move, bad_one.zone_out])
    move_choice()
    # 若hp低於0, 則被踢出隊伍
    if bad_one.hp <= 0:
        print(f'{bad_one.name} is out.')
        team_bad.remove(bad_one)
        if len(team_bad) == 0:
            print('壞人數:', len(team_bad), '英雄數:', len(team_hero))
            print('-------------------- Final result: Heroes won! --------------------')
            break
        else:
            bad_one = choice(team_bad)
    elif hero_one.hp <= 0:
        print(f'{hero_one.name} is out.')
        team_hero.remove(hero_one)
        if len(team_hero) == 0:
            print('壞人數:', len(team_bad), '英雄數:', len(team_hero))
            print('-------------------- Final result: Badass won! --------------------')
            break
        else:
            hero_one = choice(team_hero)

    # -------------- team_hero 採取動作 --------------
    bad_one.hp -= bad_one.damage(hero_one.power)
    move_choice = choice([hero_one.refill_hp, hero_one.zone_out])
    if move_choice == hero_one.refill_hp:
        move_choice(hero_one.hp)
    else:
        move_choice()
    # 若hp低於0, 則被踢出隊伍
    if bad_one.hp <= 0:
        print(f'{bad_one.name} is out.')
        team_bad.remove(bad_one)
        if len(team_bad) == 0:
            print('壞人數:', len(team_bad), '英雄數:', len(team_hero))
            print('-------------------- Final result: Heroes won! --------------------')
            break
        else:
            bad_one = choice(team_bad)
    elif hero_one.hp <= 0:
        print(f'{hero_one.name} is out.')
        team_hero.remove(hero_one)
        if len(team_hero) == 0:
            print('壞人數:', len(team_bad), '英雄數:', len(team_hero))
            print('-------------------- Final result: Badass won! --------------------')
            break
        else:
            hero_one = choice(team_hero)

    # print(f'血量值: {hero_one.name},{hero_one.hp}  v.s.  {bad_one.name},{bad_one.hp}')
    # print('壞人數:', len(team_bad), '英雄數:', len(team_hero))
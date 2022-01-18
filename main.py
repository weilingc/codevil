from world import Badass, Hero
from random import choice

# 在這個平台中，創建數個Badass類別的物件
corp_cop = Badass('Corp_cop', 50, 35, 1)
bad_cop = Badass('Bad_cop', 100, 30, 2)
kingpin = Badass('Kingpin', 600, 80, 10)

# 在這個平台中，創建數個Hero類別的物件
darevil = Hero('Darevil', 500, 70, 10)
elek = Hero('Elek', 400, 60, 5)


# Hero和Badass的對決，每一回合一對一，上場選手隨機
team_hero = [darevil, elek]
team_bad = [corp_cop, bad_cop, kingpin]

fight_round = 1
while True:

    #若隊伍中完全沒人, 則判定另一方獲勝
    if len(team_hero) == 0:
        print('Badass won!')
        break
    elif len(team_bad) == 0:
        print('Heroes won!')
        break

    # 設定打鬥的場景
    else:
        print('-------------------- round', fight_round, '--------------------')
        fight_round += 1

        # 兩隊各派出一人出來對戰
        bad_one = choice(team_bad)
        hero_one = choice(team_hero)

        # bad 採取動作
        hero_one.hp -= hero_one.damage(bad_one.power) # hero扣掉自身防禦值後的傷害值
        # bad 使用額外招式
        move_choice = choice([bad_one.dirty_move, bad_one.zone_out])
        move_choice()


        # hero 採取動作
        bad_one.hp -= bad_one.damage(hero_one.power)
        # hero 使用額外招式
        move_choice = choice([hero_one.refill_hp, hero_one.zone_out])
        if move_choice == hero_one.refill_hp:
            move_choice(hero_one.hp)
        else:
            move_choice()


        # 若hp低於0, 則被踢出隊伍
        if bad_one.hp <= 0:
            team_bad.remove(bad_one)
        elif hero_one.hp <= 0:
            team_hero.remove(hero_one)
        print(f'血量值: {hero_one.name},{hero_one.hp}  v.s.  {bad_one.name},{bad_one.hp}')
        print('壞人數:', len(team_bad), '英雄數:', len(team_hero))
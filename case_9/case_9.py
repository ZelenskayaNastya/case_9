# постоянные события
from random import random


def sell():
    return


def buy():
    return


def sow():
    return


def give():
    return

# неуправляемые события
def vor(money):
    # money - деньги из казны
    if money >= 100:
        for i in random(100, money):
            print('Король, о ужас!!! Сегодня ноью пропало', i, 'рубликов. Нужно усилить охрану!')
            new_money = money - i
    else:
        print('Король, о ужас!!! Сегодня ночью пропали все деньги из казны. Нужно усилить охрану!')
        new_money = 0
    return new_money


def flood(corn):
    # количество зерна
    if corn >= 250:
        for i in random(250, corn):
            print('Мой король, река вылилась за края и затопила поля с пшеницей. Мы потеряли', i, 'кг урожая.')
            new_corn = corn - i
    else:
        print('Мой король, река вылилась за края и затопила поля с пшеницей. Мы потеряли весь урожай.')
        new_corn = 0
    return new_corn


def nasledstvo(money, zemlya):
    # money - деньги из казны
    for i in random(1000, 1000000):
        for g in random(10000, 1000000):
            print('Пришло письмо несчастья, мой Король. Сегодня ночью скончался Ваш дальний '
                  'родственник. Оказалось, что он оставил в завещании все наследство именно вам. '
                  'Вы получили в казну', i,
                  'рубликов и', g, 'гт земли.')
            new_money = money + i
            new_zemlya = zemlya + g
    return new_money, new_zemlya


def princesa(money):
    # money - деньги из казны
    if money >= 500:
        for i in random(500, money):
            print('Король, сегодня ночью из своей спальни была похищена '
                  'Ваша дочь, вор просит выкуп в размере', i, 'рубликов.')
            new_money = money - i
    else:
        print('Король, сегодня ночью из своей спальни была похищена '
              'Ваша дочь, вор просит выкуп в размере', money, 'рубликов.')
        new_money = 0
    return new_money


def crisi(corn):
    # количество зерна
    if corn >= 250:
        for i in random(250, corn):
            print('Сегодня ночью было нашествие крыс. Крысы сумели утащить', i, 'кг зерен.')
            new_corn = corn - i
    else:
        print('Крысы сумели утащили все зерно из хранилица.')
        new_corn = 0
    return new_corn


def princesa_dress(money):
    # money - деньги из казны
    if money >= 500:
        for i in random(500, money):
            print('Король, сегодня Ваша дочь похала по магазинам выбирать себе новый '
                  'наряд для балла. Она проит', i, 'рубликов шоппинг.')
            new_money = money - i
    else:
        print('Король, сегодня Ваша дочь похала по магазинам выбирать себе новый '
              'наряд для бала. Она забрала все денежки из казны.')
        new_money = 0
    return new_money


def prazdnik(money):
    # money - деньги из казны
    if money >= 500:
        for i in random(500, money):
            print('Король, завтра в городе праздник, нужно', i,
                  'рубликов для организации праздника и украшения города.')
            new_money = money - i
    elif money < 500:
        for i in range(money):
            print('Король, завтра в городе праздник, нужно', i,
                  'рубликов для организации праздника и украшения города.')
            new_money = money - i
    return new_money


def princesa_HB(money):
    # money - деньги из казны
    if money < 500:
        for i in random(money):
            print('Король, завтра День Рождения у вашей любимой дочери, '
                  'Вам нужно выделить денежки ей на подарок в размере', i, 'рубликов)))')
            new_money = money - i

    elif money >= 500:
        for i in range(500, money):
            print('Король, завтра День Рождения у вашей любимой дочери, '
                  'Вам нужно выделить денежки ей на подарок в размере', i, 'рубликов)))')
            new_money = money - i
    return new_money




# управляемые события
def first():
    return

def main():
    date = input()


if __name__ == "__main__":
    main()
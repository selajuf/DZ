##
## Продукты и цена
##

products = {'молоко': 20,
            'сметана': 10,
            'грибы': 20,
            'картошка': 25,
            'творог': 15,
            'сок': 20,
            'колбаса': 25,
            'сыр': 20,
            'йогурт': 20,
            'мюсли': 15}
##
## Монеты в кассе
##

monets = {1: 5,
          5: 2,
          7: 2,
          10: 1,
          15: 1}


def buy():
    random_monet = int(input('Введите монету которую даёт покупатель: '))
    select_product = input(
        "\nМолоко:20\nСметана:10\nГрибы:20, \nКартошка:25, \nТворог:15, \nСок:20, \nКолбаса:25, \nСыр:20, \nЙогурт:20, \nМюсли:15\n\nВведите название продукта который вы хотите взять: ").lower()
    select_price = products.get(select_product)

    print(f'Монета у покупателя {random_monet}\n\nПродукт: {select_product}. Цена: {select_price}')

    amount = random_monet - select_price

    change = amount
    change_coins = []
    while change > 0:
        for coin in sorted(monets, reverse=True):
            while change >= coin:
                quantity_monets = monets.get(coin)
                if quantity_monets > 0:  # проверяю есть ли номинал этой монеты в кассе
                    print(f"Выдал монету - {coin}")
                    change -= coin
                    change_coins.append(coin)
                    monets[coin] -= 1  # удаление монеты этого номинала, минусую один
                else:
                    break  # конец цикла если нет номинала этой монетки

    print(f'Монеты для сдачи: {change_coins}')


buy()

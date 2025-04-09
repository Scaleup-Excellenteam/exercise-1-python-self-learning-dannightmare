"""Solution 5.2"""


def piece_of_cake(prices: dict, optionals: list, **amounts):
    """Piece of cake

    :param dict prices
    :param list optionals
    :return float price"""
    total = 0
    for product, price in prices.items():
        if product in optionals or product not in amounts:
            continue
        total += amounts[product] * price / 100

    return total

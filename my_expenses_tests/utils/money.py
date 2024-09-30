def int_to_str(value, currency):
    return f'{currency}{float(value):,.02f}'


def define_currency(name):
    currency_dict = {'US Dollar': '$', 'Euro': '€', 'Indonesian Rupiah': 'IDR', 'Australian Dollar': 'A$'}
    return currency_dict[name]
